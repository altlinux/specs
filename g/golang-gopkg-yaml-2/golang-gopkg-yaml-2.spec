%def_without check

%global goipath         gopkg.in/yaml.v2
%global forgeurl        https://github.com/go-yaml/yaml

%global goaltipaths     gopkg.in/v2/yaml

Name: golang-gopkg-yaml-2
Version: 2.4.0
Release: alt1
Summary: Yaml support for the Go language
Group: Development/Other
License: Apache-2.0 and MIT
Url: https://github.com/go-yaml/yaml
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/yaml-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and is
based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package supports most of YAML 1.1 and 1.2, including support for
anchors, tags, map merging, etc. Multi-document unmarshalling is not yet
implemented, and base-60 floats from YAML 1.1 are purposefully not supported
since they're a poor design and are gone in YAML 1.2.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n yaml-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc LICENSE LICENSE.libyaml NOTICE README.md
%go_path/src/%goipath

%changelog
* Mon Dec 28 2020 Leontiy Volodin <lvol@altlinux.org> 2.4.0-alt1
- New version.

* Sat Aug 08 2020 Leontiy Volodin <lvol@altlinux.org> 2.3.0-alt1
- New version.

* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 2.2.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

