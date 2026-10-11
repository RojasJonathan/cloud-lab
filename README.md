# Cloud GRC Lab

## Project Overview

This project is a hands-on cloud governance, risk, and compliance (GRC) lab built using AWS, Terraform, GitHub, and HCP Terraform.

The goal is to gain practical experience with cloud infrastructure, infrastructure as code (IaC), policy as code (PaC), and cloud security controls.

The project approaches cloud security from a GRC perspective, focusing on how organizations can establish, enforce, and assess security requirements across cloud environments.

## Project Objectives

- Deploy and manage AWS resources using Terraform.
- Learn how infrastructure as code supports consistent cloud configurations.
- Explore preventive security controls using Sentinel policy as code.
- Understand how cloud security requirements translate into technical configurations.
- Develop practical cloud GRC skills through hands-on testing.
- Build a portfolio demonstrating cloud governance and compliance knowledge.

## Technologies Used

| Technology | Purpose |
|---|---|
| AWS | Cloud environment hosting lab resources |
| Terraform | Defines and provisions infrastructure using code |
| HCP Terraform | Manages Terraform runs and policy evaluations |
| Sentinel | Defines and evaluates policy-as-code rules |
| GitHub | Stores and tracks infrastructure code |
| GitHub Actions | Supports Terraform automation workflows |

## Work Completed

### 1. GitHub Repository and Terraform Setup

Created a GitHub repository to store and manage the cloud lab's infrastructure code.

Configured the Terraform project to work with HCP Terraform.

Key concepts explored:

- Version control and code repositories
- Terraform configuration files (`.tf`)
- GitHub Actions workflow files (`.yml`)
- Terraform plan and apply operations
- Managing infrastructure through code rather than manual configuration

### 2. AWS S3 Bucket Deployment

Provisioned an Amazon S3 bucket using Terraform.

The bucket serves as an initial cloud resource for learning infrastructure provisioning and security configuration.

Security configurations include:

| Configuration | Setting |
|---|---|
| S3 bucket prefix | `grc-cloud-lab-` |
| Public access blocking | Enabled |
| Bucket versioning | Enabled |
| Resource provisioning | Terraform |

The Terraform configuration also includes an output named `evidence_bucket_name`, which returns the generated bucket name.

These configurations introduce cloud security concepts such as preventing unintended public access, preserving object versions, and maintaining consistent resource configurations.

### 3. HCP Terraform and Sentinel Policy as Code

Configured a Sentinel policy set in HCP Terraform and tested a policy using advisory enforcement.

Sentinel allows organizations to evaluate infrastructure configurations against defined rules during the Terraform workflow.

Key concepts explored:

- Policy as code
- Policy sets
- Policy enforcement modes
- Evaluating infrastructure configurations against security requirements
- Identifying noncompliant configurations before deployment

Advisory enforcement was used to understand policy evaluation without automatically blocking infrastructure changes.

This introduces the concept of preventive cloud governance, where security requirements can be evaluated before resources are deployed.

## Cloud GRC Relevance

This lab demonstrates how cloud governance requirements can be translated into technical controls.

For example:

| GRC Requirement | Technical Approach |
|---|---|
| Restrict public access to cloud storage | S3 public access block configuration |
| Support object version recovery | S3 bucket versioning |
| Establish consistent infrastructure configurations | Terraform |
| Evaluate infrastructure against defined policies | Sentinel |
| Maintain infrastructure configuration history | GitHub version control |

These capabilities can support cloud security governance, compliance assessments, and audit activities.

## Project Roadmap

The lab will continue expanding beyond the initial S3 deployment.

Planned areas include:

- Python scripting for cloud security analysis
- AWS Config for configuration and compliance monitoring
- Additional AWS resources and security configurations
- Expanded Sentinel policies and enforcement testing
- Cloud security dashboards and reporting
- Security control mapping to recognized frameworks
- Risk assessments and compliance documentation
- Mock audit testing and evidence collection
- Cloud architecture diagrams and shared responsibility mapping
- Final portfolio documentation

These items are planned and have not yet been completed.

## Project Goal

The long-term goal is to develop a cloud GRC portfolio that demonstrates both technical cloud knowledge and the ability to evaluate cloud security controls from a governance, risk, and compliance perspective.

The project will continue to evolve as new cloud services, security controls, and compliance testing capabilities are introduced.
