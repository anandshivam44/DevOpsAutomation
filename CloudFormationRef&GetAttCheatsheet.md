| Resource Type | Ref | GetAtt |
| --- | --- | --- |
| Alexa::ASK::Skill | Id  |     |
| AWS::AmazonMQ::Broker | Id  | AmqpEndpoints, Arn, ConfigurationId, ConfigurationRevision, IpAddresses, MqttEndpoints, OpenWireEndpoints, StompEndpoints, WssEndpoints |
| AWS::AmazonMQ::Configuration | Id  | Arn, Id, Revision |
| AWS::AmazonMQ::ConfigurationAssociation | Id  |     |
| AWS::Amplify::App | –   | AppId, AppName, Arn, DefaultDomain |
| AWS::Amplify::Branch | –   | Arn, BranchName |
| AWS::Amplify::Domain | –   | Arn, CertificateRecord, DomainName, DomainStatus, StatusReason |
| AWS::ApiGateway::Account | Id  |     |
| AWS::ApiGateway::ApiKey | Id  |     |
| AWS::ApiGateway::Authorizer | Id  |     |
| AWS::ApiGateway::BasePathMapping | –   |     |
| AWS::ApiGateway::ClientCertificate | Name |     |
| AWS::ApiGateway::Deployment | Id  |     |
| AWS::ApiGateway::DocumentationPart | Id  |     |
| AWS::ApiGateway::DocumentationVersion | –   |     |
| AWS::ApiGateway::DomainName | DomainName | DistributionDomainName, DistributionHostedZoneId, RegionalDomainName, RegionalHostedZoneId |
| AWS::ApiGateway::GatewayResponse | –   |     |
| AWS::ApiGateway::Method | Id  |     |
| AWS::ApiGateway::Model | Name |     |
| AWS::ApiGateway::RequestValidator | Id  |     |
| AWS::ApiGateway::Resource | Id  |     |
| AWS::ApiGateway::RestApi | Id  | RootResourceId |
| AWS::ApiGateway::Stage | Name |     |
| AWS::ApiGateway::UsagePlan | Id  |     |
| AWS::ApiGateway::UsagePlanKey | –   |     |
| AWS::ApiGateway::VpcLink | Id  |     |
| AWS::ApiGatewayV2::Api | Id  |     |
| AWS::ApiGatewayV2::ApiMapping | Id  |     |
| AWS::ApiGatewayV2::Authorizer | Id  |     |
| AWS::ApiGatewayV2::Deployment | Id  |     |
| AWS::ApiGatewayV2::DomainName | DomainName | RegionalDomainName, RegionalHostedZoneId |
| AWS::ApiGatewayV2::Integration | Id  |     |
| AWS::ApiGatewayV2::IntegrationResponse | Id  |     |
| AWS::ApiGatewayV2::Model | Id  |     |
| AWS::ApiGatewayV2::Route | Id  |     |
| AWS::ApiGatewayV2::RouteResponse | Id  |     |
| AWS::ApiGatewayV2::Stage | Name |     |
| AWS::ApplicationAutoScaling::ScalableTarget | Id  |     |
| AWS::ApplicationAutoScaling::ScalingPolicy | Arn |     |
| AWS::AppMesh::Mesh | Arn | Arn, MeshName, Uid |
| AWS::AppMesh::Route | Arn | Arn, MeshName, Uid, VirtualRouterName |
| AWS::AppMesh::VirtualNode | Arn | Arn, MeshName, Uid, VirtualNodeName |
| AWS::AppMesh::VirtualRouter | Arn | Arn, MeshName, Uid, VirtualRouterName |
| AWS::AppMesh::VirtualService | Arn | Arn, MeshName, Uid, VirtualServiceName |
| AWS::AppSync::ApiKey | Arn | ApiKey, Arn |
| AWS::AppSync::DataSource | Arn | DataSourceArn, Name |
| AWS::AppSync::FunctionConfiguration | Arn | DataSourceName, FunctionArn, FunctionId, Name |
| AWS::AppSync::GraphQLApi | Arn | ApiId, Arn, GraphQLUrl |
| AWS::AppSync::GraphQLSchema | Id  |     |
| AWS::AppSync::Resolver | Arn | FieldName, ResolverArn, TypeName |
| AWS::Athena::NamedQuery | Name |     |
| AWS::AutoScaling::AutoScalingGroup | Name |     |
| AWS::AutoScaling::LaunchConfiguration | Name |     |
| AWS::AutoScaling::LifecycleHook | Name |     |
| AWS::AutoScaling::ScalingPolicy | Arn |     |
| AWS::AutoScaling::ScheduledAction | Name |     |
| AWS::AutoScalingPlans::ScalingPlan | Arn |     |
| AWS::Backup::BackupPlan | Id  | BackupPlanArn, BackupPlanId, VersionId |
| AWS::Backup::BackupSelection | Id  | BackupPlanId, SelectionId |
| AWS::Backup::BackupVault | Name | BackupVaultArn, BackupVaultName |
| AWS::Batch::ComputeEnvironment | Arn |     |
| AWS::Batch::JobDefinition | Arn |     |
| AWS::Batch::JobQueue | Arn |     |
| AWS::Budgets::Budget | Name |     |
| AWS::CertificateManager::Certificate | Arn |     |
| AWS::CloudFormation::CustomResource | –   |     |
| AWS::CloudFormation::Macro | Name |     |
| AWS::CloudFormation::Stack | Id  |     |
| AWS::CloudFormation::WaitCondition | Name | Data |
| AWS::CloudFormation::WaitConditionHandle | –   |     |
| AWS::CloudFront::CloudFrontOriginAccessIdentity | OriginAccessIdentity | S3CanonicalUserId |
| AWS::CloudFront::Distribution | Id  | DomainName |
| AWS::CloudFront::StreamingDistribution | Id  | DomainName |
| AWS::CloudTrail::Trail | Name | Arn, SnsTopicArn |
| AWS::CloudWatch::Alarm | Name | Arn |
| AWS::CloudWatch::AnomalyDetector | –   |     |
| AWS::CloudWatch::Dashboard | Name |     |
| AWS::CodeBuild::Project | Name | Arn |
| AWS::CodeCommit::Repository | Id  | Arn, CloneUrlHttp, CloneUrlSsh, Name |
| AWS::CodeDeploy::Application | Name |     |
| AWS::CodeDeploy::DeploymentConfig | Name |     |
| AWS::CodeDeploy::DeploymentGroup | Name |     |
| AWS::CodePipeline::CustomActionType | Name |     |
| AWS::CodePipeline::Pipeline | Name | Version |
| AWS::CodePipeline::Webhook | Name | Url |
| AWS::Cognito::IdentityPool | Id  | Name |
| AWS::Cognito::IdentityPoolRoleAttachment | Id  |     |
| AWS::Cognito::UserPool | Id  | Arn, ProviderName, ProviderURL |
| AWS::Cognito::UserPoolClient | Id  |     |
| AWS::Cognito::UserPoolGroup | Name |     |
| AWS::Cognito::UserPoolUser | Name |     |
| AWS::Cognito::UserPoolUserToGroupAttachment | Id  |     |
| AWS::Config::AggregationAuthorization | Arn |     |
| AWS::Config::ConfigRule | Name | Arn, Compliance.Type, ConfigRuleId |
| AWS::Config::ConfigurationAggregator | Name |     |
| AWS::Config::ConfigurationRecorder | Name |     |
| AWS::Config::DeliveryChannel | Name |     |
| AWS::Config::RemediationConfiguration | RemediationAction |     |
| AWS::DataPipeline::Pipeline | Id  |     |
| AWS::DAX::Cluster | Name | Arn, ClusterDiscoveryEndpoint |
| AWS::DAX::ParameterGroup | Name |     |
| AWS::DAX::SubnetGroup | Name |     |
| AWS::DLM::LifecyclePolicy | Id  | Arn |
| AWS::DMS::Certificate | Arn |     |
| AWS::DMS::Endpoint | Arn | ExternalId |
| AWS::DMS::EventSubscription | Name |     |
| AWS::DMS::ReplicationInstance | Arn | ReplicationInstancePrivateIpAddresses, ReplicationInstancePublicIpAddresses |
| AWS::DMS::ReplicationSubnetGroup | Name |     |
| AWS::DMS::ReplicationTask | Arn |     |
| AWS::DocDB::DBCluster | DBClusterIdentifier | ClusterResourceId, Endpoint, Port, ReadEndpoint |
| AWS::DocDB::DBClusterParameterGroup | Name |     |
| AWS::DocDB::DBInstance | Name | Endpoint, Port |
| AWS::DocDB::DBSubnetGroup | Name |     |
| AWS::DynamoDB::Table | Name | Arn, StreamArn |
| AWS::EC2::CapacityReservation | Id  | AvailabilityZone, AvailableInstanceCount, InstanceType, Tenancy, TotalInstanceCount |
| AWS::EC2::ClientVpnAuthorizationRule | –   |     |
| AWS::EC2::ClientVpnEndpoint | Id  |     |
| AWS::EC2::ClientVpnRoute | –   |     |
| AWS::EC2::ClientVpnTargetNetworkAssociation | Id  |     |
| AWS::EC2::CustomerGateway | Id  |     |
| AWS::EC2::DHCPOptions | Name |     |
| AWS::EC2::EC2Fleet | Id  |     |
| AWS::EC2::EgressOnlyInternetGateway | Id  |     |
| AWS::EC2::EIP | ElasticIpAddress | AllocationId |
| AWS::EC2::EIPAssociation | Name |     |
| AWS::EC2::FlowLog | Id  |     |
| AWS::EC2::Host | Id  |     |
| AWS::EC2::Instance | Id  | AvailabilityZone, PrivateDnsName, PrivateIp, PublicDnsName, PublicIp |
| AWS::EC2::InternetGateway | Name |     |
| AWS::EC2::LaunchTemplate | Id  | DefaultVersionNumber, LatestVersionNumber |
| AWS::EC2::NatGateway | Name |     |
| AWS::EC2::NetworkAcl | Name |     |
| AWS::EC2::NetworkAclEntry | Name |     |
| AWS::EC2::NetworkInterface | Name | PrimaryPrivateIpAddress, SecondaryPrivateIpAddresses |
| AWS::EC2::NetworkInterfaceAttachment | Name |     |
| AWS::EC2::NetworkInterfacePermission | Name |     |
| AWS::EC2::PlacementGroup | Name |     |
| AWS::EC2::Route | Id  |     |
| AWS::EC2::RouteTable | Id  |     |
| AWS::EC2::SecurityGroup | Name | GroupId, VpcId |
| AWS::EC2::SecurityGroupEgress | RuleName |     |
| AWS::EC2::SecurityGroupIngress | –   |     |
| AWS::EC2::SpotFleet | Id  |     |
| AWS::EC2::Subnet | Id  | AvailabilityZone, Ipv6CidrBlocks, NetworkAclAssociationId, VpcId |
| AWS::EC2::SubnetCidrBlock | CidrBlock |     |
| AWS::EC2::SubnetNetworkAclAssociation | Id  | AssociationId |
| AWS::EC2::SubnetRouteTableAssociation | Id  |     |
| AWS::EC2::TransitGateway | Id  |     |
| AWS::EC2::TransitGatewayAttachment | Name |     |
| AWS::EC2::TransitGatewayRoute | Name |     |
| AWS::EC2::TransitGatewayRouteTable | Name |     |
| AWS::EC2::TransitGatewayRouteTableAssociation | Id  |     |
| AWS::EC2::TransitGatewayRouteTablePropagation | RouteTableId |     |
| AWS::EC2::Volume | Name |     |
| AWS::EC2::VolumeAttachment | –   |     |
| AWS::EC2::VPC | Id  | CidrBlock, CidrBlockAssociations, DefaultNetworkAcl, DefaultSecurityGroup, Ipv6CidrBlocks |
| AWS::EC2::VPCCidrBlock | CidrBlock |     |
| AWS::EC2::VPCDHCPOptionsAssociation | Id  |     |
| AWS::EC2::VPCEndpoint | Id  | CreationTimestamp, DnsEntries, NetworkInterfaceIds |
| AWS::EC2::VPCEndpointConnectionNotification | Id  |     |
| AWS::EC2::VPCEndpointService | Id  |     |
| AWS::EC2::VPCEndpointServicePermissions | Id  |     |
| AWS::EC2::VPCGatewayAttachment | Id  |     |
| AWS::EC2::VPCPeeringConnection | Id  |     |
| AWS::EC2::VPNConnection | Id  |     |
| AWS::EC2::VPNConnectionRoute | Id  |     |
| AWS::EC2::VPNGateway | Id  |     |
| AWS::EC2::VPNGatewayRoutePropagation | VpnGatewayId |     |
| AWS::ECR::Repository | Name | Arn |
| AWS::ECS::Cluster | Name | Arn |
| AWS::ECS::Service | Arn | Name |
| AWS::ECS::TaskDefinition | Arn |     |
| AWS::EFS::FileSystem | Id  |     |
| AWS::EFS::MountTarget | Id  | IpAddress |
| AWS::EKS::Cluster | Name | Arn, CertificateAuthorityData, Endpoint |
| AWS::ElastiCache::CacheCluster | Name | ConfigurationEndpoint.Address, ConfigurationEndpoint.Port, RedisEndpoint.Address, RedisEndpoint.Port |
| AWS::ElastiCache::ParameterGroup | Name |     |
| AWS::ElastiCache::ReplicationGroup | Name | ConfigurationEndPoint.Address, ConfigurationEndPoint.Port, PrimaryEndPoint.Address, PrimaryEndPoint.Port, ReadEndPoint.Addresses, ReadEndPoint.Addresses.List, ReadEndPoint.Ports, ReadEndPoint.Ports.List |
| AWS::ElastiCache::SecurityGroup | Name |     |
| AWS::ElastiCache::SecurityGroupIngress | Name |     |
| AWS::ElastiCache::SubnetGroup | Name |     |
| AWS::ElasticBeanstalk::Application | Name |     |
| AWS::ElasticBeanstalk::ApplicationVersion | Name |     |
| AWS::ElasticBeanstalk::ConfigurationTemplate | Name |     |
| AWS::ElasticBeanstalk::Environment | Name | EndpointURL |
| AWS::ElasticLoadBalancing::LoadBalancer | Name | CanonicalHostedZoneName, CanonicalHostedZoneNameID, DNSName, SourceSecurityGroup.GroupName, SourceSecurityGroup.OwnerAlias |
| AWS::ElasticLoadBalancingV2::Listener | Arn |     |
| AWS::ElasticLoadBalancingV2::ListenerCertificate | –   |     |
| AWS::ElasticLoadBalancingV2::ListenerRule | Arn |     |
| AWS::ElasticLoadBalancingV2::LoadBalancer | Arn | CanonicalHostedZoneID, DNSName, LoadBalancerFullName, LoadBalancerName, SecurityGroups |
| AWS::ElasticLoadBalancingV2::TargetGroup | Arn | LoadBalancerArns, TargetGroupFullName, TargetGroupName |
| AWS::Elasticsearch::Domain | Name | Arn, DomainArn, DomainEndpoint |
| AWS::EMR::Cluster | Id  | MasterPublicDNS |
| AWS::EMR::InstanceFleetConfig | InstanceFleetId |     |
| AWS::EMR::InstanceGroupConfig | InstanceGroupId |     |
| AWS::EMR::SecurityConfiguration | Name |     |
| AWS::EMR::Step | Id  |     |
| AWS::Events::EventBus | Name | Arn, Name, Policy |
| AWS::Events::EventBusPolicy | Id  |     |
| AWS::Events::Rule | Id  | Arn |
| AWS::Glue::Classifier | Name |     |
| AWS::Glue::Connection | Name |     |
| AWS::Glue::Crawler | Name |     |
| AWS::Glue::Database | Name |     |
| AWS::Glue::DataCatalogEncryptionSettings | –   |     |
| AWS::Glue::DevEndpoint | Name |     |
| AWS::Glue::Job | Name |     |
| AWS::Glue::Partition | Name |     |
| AWS::Glue::SecurityConfiguration | –   |     |
| AWS::Glue::Table | Name |     |
| AWS::Glue::Trigger | Name |     |
| AWS::GuardDuty::Detector | Id  |     |
| AWS::GuardDuty::Filter | Name |     |
| AWS::GuardDuty::IPSet | Id  |     |
| AWS::GuardDuty::Master | AccountId |     |
| AWS::GuardDuty::Member | AccountId |     |
| AWS::GuardDuty::ThreatIntelSet | Id  |     |
| AWS::IAM::AccessKey | AccessKeyId | SecretAccessKey |
| AWS::IAM::Group | Name | Arn |
| AWS::IAM::InstanceProfile | Name | Arn |
| AWS::IAM::ManagedPolicy | Arn |     |
| AWS::IAM::Policy | Name |     |
| AWS::IAM::Role | Name | Arn, RoleId |
| AWS::IAM::ServiceLinkedRole | –   |     |
| AWS::IAM::User | UserName | Arn |
| AWS::IAM::UserToGroupAddition | Name |     |
| AWS::Inspector::AssessmentTarget | –   | Arn |
| AWS::Inspector::AssessmentTemplate | –   | Arn |
| AWS::Inspector::ResourceGroup | –   | Arn |
| AWS::IoT::Certificate | Id  | Arn |
| AWS::IoT::Policy | Name | Arn |
| AWS::IoT::PolicyPrincipalAttachment | –   |     |
| AWS::IoT::Thing | Name |     |
| AWS::IoT::ThingPrincipalAttachment | –   |     |
| AWS::IoT::TopicRule | Name | Arn |
| AWS::IoT1Click::Device | Arn | Arn, DeviceId, Enabled |
| AWS::IoT1Click::Placement | Id  | PlacementName, ProjectName |
| AWS::IoT1Click::Project | Arn | Arn, ProjectName |
| AWS::IoTAnalytics::Channel | –   |     |
| AWS::IoTAnalytics::Dataset | –   |     |
| AWS::IoTAnalytics::Datastore | –   |     |
| AWS::IoTAnalytics::Pipeline | –   |     |
| AWS::IoTEvents::DetectorModel | Name |     |
| AWS::IoTEvents::Input | Name |     |
| AWS::IoTThingsGraph::FlowTemplate | Urn |     |
| AWS::Kinesis::Stream | Name | Arn |
| AWS::Kinesis::StreamConsumer | ConsumerArn | ConsumerARN, ConsumerCreationTimestamp, ConsumerName, ConsumerStatus, StreamARN |
| AWS::KinesisAnalytics::Application | –   |     |
| AWS::KinesisAnalytics::ApplicationOutput | –   |     |
| AWS::KinesisAnalytics::ApplicationReferenceDataSource | –   |     |
| AWS::KinesisAnalyticsV2::Application | –   |     |
| AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption | –   |     |
| AWS::KinesisAnalyticsV2::ApplicationOutput | –   |     |
| AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource | –   |     |
| AWS::KinesisFirehose::DeliveryStream | Name | Arn |
| AWS::KMS::Alias | Name |     |
| AWS::KMS::Key | Id  | Arn |
| AWS::Lambda::Alias | Arn |     |
| AWS::Lambda::EventSourceMapping | Name |     |
| AWS::Lambda::Function | Name | Arn |
| AWS::Lambda::LayerVersion | Arn |     |
| AWS::Lambda::LayerVersionPermission | Arn |     |
| AWS::Lambda::Permission | –   |     |
| AWS::Lambda::Version | Arn | Version |
| AWS::Logs::Destination | Name | Arn |
| AWS::Logs::LogGroup | Name | Arn |
| AWS::Logs::LogStream | Name |     |
| AWS::Logs::MetricFilter | –   |     |
| AWS::Logs::SubscriptionFilter | Name |     |
| AWS::RDS::DBCluster | Name | Endpoint.Address, Endpoint.Port, ReadEndpoint.Address |
| AWS::RDS::DBClusterParameterGroup | Name |     |
| AWS::RDS::DBInstance | Name | Endpoint.Address, Endpoint.Port |
| AWS::RDS::DBParameterGroup | Name |     |
| AWS::RDS::DBSecurityGroup | Name |     |
| AWS::RDS::DBSecurityGroupIngress | DBSecurityGroup |     |
| AWS::RDS::DBSubnetGroup | Name |     |
| AWS::RDS::EventSubscription | Name |     |
| AWS::RDS::OptionGroup | Name |     |
| AWS::Route53::HealthCheck | HealthCheckId |     |
| AWS::Route53::HostedZone | HosteadZoneId | NameServers |
| AWS::Route53::RecordSet | DomainName |     |
| AWS::Route53::RecordSetGroup | Name |     |
| AWS::Route53Resolver::ResolverEndpoint | ResolverEndpoint | Arn, Direction, HostVPCId, IpAddressCount, Name, ResolverEndpointId |
| AWS::Route53Resolver::ResolverRule | ResolverRule | Arn, DomainName, ResolverEndpointId, ResolverRuleId, TargetIps |
| AWS::Route53Resolver::ResolverRuleAssociation | ResolverRuleAssociationId | Name, ResolverRuleAssociationId, ResolverRuleId, VPCId |
| AWS::S3::Bucket | Name | Arn, DomainName, DualStackDomainName, RegionalDomainName, WebsiteURL |
| AWS::SageMaker::CodeRepository | Arn | CodeRepositoryName |
| AWS::SageMaker::Endpoint | Arn | EndpointName |
| AWS::SageMaker::EndpointConfig | Arn | EndpointConfigName |
| AWS::SageMaker::Model | Arn | ModelName |
| AWS::SageMaker::NotebookInstance | Arn | NotebookInstanceName |
| AWS::SageMaker::NotebookInstanceLifecycleConfig | Arn | NotebookInstanceLifecycleConfigName |
| AWS::SecretsManager::ResourcePolicy | Arn |     |
| AWS::SecretsManager::RotationSchedule | Arn |     |
| AWS::SecretsManager::Secret | Arn |     |
| AWS::SecretsManager::SecretTargetAttachment | Arn |     |
| AWS::ServiceDiscovery::HttpNamespace | Id  | Arn, Id |
| AWS::ServiceDiscovery::Instance | Id  |     |
| AWS::ServiceDiscovery::PrivateDnsNamespace | Id  | Arn, Id |
| AWS::ServiceDiscovery::PublicDnsNamespace | Id  | Arn, Id |
| AWS::ServiceDiscovery::Service | Id  | Arn, Id, Name |
| AWS::SES::ConfigurationSet | Name |     |
| AWS::SES::ConfigurationSetEventDestination |     |     |
| AWS::SES::ReceiptFilter |     |     |
| AWS::SES::ReceiptRule | Name |     |
| AWS::SES::ReceiptRuleSet | Name |     |
| AWS::SES::Template |     |     |
| AWS::SNS::Topic | Arn | TopicName |
| AWS::SQS::Queue | QueueURL | Arn, QueueName |
| AWS::SSM::Association |     |     |
| AWS::SSM::Document | Name |     |
| AWS::SSM::MaintenanceWindow | Id  |     |
| AWS::SSM::MaintenanceWindowTarget | Id  |     |
| AWS::SSM::MaintenanceWindowTask | Id  |     |
| AWS::SSM::Parameter | Name | Type, Value |
| AWS::SSM::PatchBaseline | Id  |     |
| AWS::SSM::ResourceDataSync | Name |     |
| AWS::StepFunctions::Activity | Arn | Name |
| AWS::StepFunctions::StateMachine | Arn | Name |
| AWS::Transfer::Server | Id  | Arn, ServerId |
| AWS::Transfer::User | UserName | Arn, ServerId, UserName |
| AWS::WAF::ByteMatchSet | Id  |     |
| AWS::WAF::IPSet | Id  |     |
| AWS::WAF::Rule | Id  |     |
| AWS::WAF::SizeConstraintSet | Id  |     |
| AWS::WAF::SqlInjectionMatchSet | Id  |     |
| AWS::WAF::WebACL | Name |     |
| AWS::WAF::XssMatchSet | Id  |     |
| AWS::WAFRegional::ByteMatchSet | Id  |     |
| AWS::WAFRegional::GeoMatchSet | Id  |     |
| AWS::WAFRegional::IPSet | Id  |     |
| AWS::WAFRegional::RateBasedRule | Id  |     |
| AWS::WAFRegional::RegexPatternSet | Id  |     |
| AWS::WAFRegional::Rule | Id  |     |
| AWS::WAFRegional::SizeConstraintSet | Id  |     |
| AWS::WAFRegional::SqlInjectionMatchSet | Id  |     |
| AWS::WAFRegional::WebACL | Name |     |
| AWS::WAFRegional::WebACLAssociation |     |     |
