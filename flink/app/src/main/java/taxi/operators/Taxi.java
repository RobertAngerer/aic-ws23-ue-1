package taxi.operators;

import java.time.Instant;

public record Taxi(String id, Instant timestamp, Double latitude, Double longitude) {}
