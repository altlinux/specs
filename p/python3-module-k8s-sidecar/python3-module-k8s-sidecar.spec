%define _unpackaged_files_terminate_build 1

%def_without check

%define pypi_name k8s-sidecar

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1

Summary: Collects config maps and stores the included files in a local folder
License: MIT
Group: Other
Url: https://github.com/kiwigrid/k8s-sidecar
Vcs: https://github.com/kiwigrid/k8s-sidecar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 python3-module-hatchling
Requires: python3-module-kubernetes-client
Requires: python3-module-requests
Requires: python3-module-python-json-logger
Requires: python3-module-logfmter

# Provided by python3-module-requests
%add_python3_req_skip requests.packages.urllib3.util.retry

BuildArch: noarch

Source: %name-%version.tar
Patch: python3-module-k8s-sidecar-2.5.0-alt-introduce-pyproject.patch

%description
This is a docker container intended to run inside a kubernetes cluster
to collect config maps with a specified label and store the included files
in an local folder. It can also send an HTTP request to a specified URL after
a configmap change. The main target is to be run as a sidecar container
to supply an application with information from the cluster.

%prep
%setup -n %name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/k8s-sidecar
%python3_sitelibdir/%{pep427_name %pypi_name}/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Feb 22 2026 Alexander Stepchenko <geochip@altlinux.org> 2.5.0-alt1
- Initial build.
