# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname right_aws

Name: ruby-%pkgname
Version: 2.0.1
Release: alt1

Summary: RightScale Amazon Web Services Ruby Modules
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/rightscale/right_aws

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Apr 26 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
The RightScale AWS modules have been designed to provide a robust, fast,
and secure interface to Amazon EC2, EBS, S3, SQS, SDB, and CloudFront.
These modules have been used in production by RightScale since late 2006
and are being maintained to track enhancements made by Amazon.

The RightScale AWS modules comprise:

- RightAws::Ec2 -- interface to Amazon EC2 (Elastic Compute Cloud), VPC
  (Virtual Private Cloud) and the associated EBS (Elastic Block Store)
- RightAws::S3 and RightAws::S3Interface -- interface to Amazon S3
  (Simple Storage Service)
- RightAws::Sqs and RightAws::SqsInterface -- interface to
  first-generation Amazon SQS (Simple Queue Service)
- RightAws::SqsGen2 and RightAws::SqsGen2Interface -- interface to
  second-generation Amazon SQS (Simple Queue Service)
- RightAws::SdbInterface and RightAws::ActiveSdb -- interface to Amazon
  SDB (SimpleDB)
- RightAws::AcfInterface -- interface to Amazon CloudFront, a content
  distribution service
- RightAws::AsInterface  -- interface to Amazon Auto Scaling
- RightAws::AcwInterface -- interface to Amazon Cloud Watch
- RightAws::ElbInterface -- interface to Amazon Elastic Load Balancer
- RightAws::RdsInterface -- interface to Amazon RDS instances

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
# RightAws::AwsError: AWS access keys are required to operate on %%SERVICENAME%%
#ruby_test_unit -Ilib:test test

%install
%ruby_install
%rdoc lib/

%files
%doc README.txt
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/RightAws

%changelog
* Thu Dec 09 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt1
- [2.0.1]

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 1.11.0-alt1
- Built for Sisyphus

