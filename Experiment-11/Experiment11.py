# Experiment 11
# HMAC System and Message Integrity Verification
import hmac
import hashlib
# Define secret key
secret_key = b"mysecretkey"
# Enter original message
original_message = input("Enter the Original Message: ")
# Generate original HMAC
original_hmac = hmac.new(
    secret_key,
    original_message.encode(),
    hashlib.sha256
).hexdigest()
print("\nGenerated HMAC:")
print(original_hmac)
# Enter received message
received_message = input("\nEnter the Received Message: ")
# Generate received message HMAC
received_hmac = hmac.new(
    secret_key,
    received_message.encode(),
    hashlib.sha256
).hexdigest()

print("\nReceived HMAC:")
print(received_hmac)
# Verify message integrity
print("\n" + "=" * 45)
print("          VERIFICATION RESULT")
print("=" * 45)
if hmac.compare_digest(original_hmac, received_hmac):
    print("Message Integrity Verified.")
    print("No Tampering Detected.")
else:
    print("Message Tampering Detected.")
    print("Integrity Verification Failed.")
