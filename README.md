# Secrets usage

## Introduction

This repository describes several possible ways of storing secrets in your application. The general purpose is to characterize each approach and define its use cases.

Considered criterias:

**Security** is a possibility of leaking secrets to undesirable parts (persons).

**Access Control** provides the ability to configure fine granular access controls on each object and component to accomplish the Least Privilege principle.

**Auditing** simply tracks who requested a secret and for what system and role.

**Secrets Management** is responsible for control over the secret lifecycle (creation, rotation, revocation, expiration)

**Implementation Complexity**

### Guide

- Storing as a plaintext
- Storing as a ciphertext
- Storing in the dedicated database
- Using cloud solutions
