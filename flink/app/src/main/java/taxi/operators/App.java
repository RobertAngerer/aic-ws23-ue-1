package taxi.operators;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.formats.json.JsonDeserializationSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class App {
  public String getGreeting() {
    return "Hello World!";
  }

  public static void main(String[] args) {

    JsonDeserializationSchema<Taxi> jsonFormat = new JsonDeserializationSchema<>(Taxi.class);
    KafkaSource<Taxi> source =
        KafkaSource.<Taxi>builder()
            .setBootstrapServers("localhost:9092")
            .setValueOnlyDeserializer(jsonFormat)
            .setTopics("taxis")
            .setGroupId("test")
            .setStartingOffsets(OffsetsInitializer.earliest())
            .build();

    StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
    DataStream<Taxi> taxis =
        env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source").name("taxis");

    System.out.println(new App().getGreeting());
  }
}
