%define _unpackaged_files_terminate_build 1

%global import_path github.com/jkroepke/kube-webhook-certgen

Name: kube-webhook-certgen
Version: 1.7.7
Release: alt1

Summary: Tools to help with self signed cert generation for Kubernetes test environment (fork of ingress-nginx)
License: Apache-2.0
Group: Other
Url: https://github.com/jkroepke/kube-webhook-certgen
Vcs: https://github.com/jkroepke/kube-webhook-certgen

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.5

%description
Generates a CA and leaf certificate with a long (100y) expiration,
then patches Kubernetes Admission Webhooks by setting the caBundle field
with the generated CA. Can optionally patch the hooks failurePolicy
setting - useful in cases where a single Helm chart needs to provision
resources and hooks at the same time as patching.

The utility works in two parts, optimized to work better with the Helm
provisioning process that leverages pre-install and post-install hooks
to execute this as a Kubernetes job.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/kube-webhook-certgen

%changelog
* Mon Feb 23 2026 Alexander Stepchenko <geochip@altlinux.org> 1.7.7-alt1
- Initial build.
