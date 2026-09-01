%define _unpackaged_files_terminate_build 1

Name: conftest
Version: 0.69.0
Release: alt1

Summary: Conftest validates config files against Rego policies
License: Apache-2.0
Group: Development/Tools
Url: https://www.conftest.dev/
Vcs: https://github.com/open-policy-agent/conftest

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Conftest helps you write tests against structured configuration data.
Using Conftest you can write tests for your Kubernetes configuration,
Tekton pipeline definitions, Terraform code, Serverless configs or
any other config files.
Conftest uses the Rego language from Open Policy Agent
for writing the assertions. You can read more about Rego in
the Policy Language section in the Open Policy Agent documentation.

%prep
%setup -a1

%build
export LDFLAGS='-X=github.com/open-policy-agent/conftest/internal/'\
'version.Version=v%version'
%gobuild -mod=vendor

%install
install -Dm0755 %name %buildroot%_bindir/%name

%files
%doc LICENSE *.md docs contrib
%_bindir/%name

%changelog
* Tue Aug 11 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.69.0-alt1
- v0.69.0.

* Thu Jul 23 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.68.2-alt1
- Initial build for Sisyphus.

