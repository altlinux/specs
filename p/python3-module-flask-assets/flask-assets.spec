%define  srcname flask-assets

Name:    python3-module-%srcname
Version: 2.0
Release: alt1

Summary: Asset management for flask
License: BSD
Group:   Development/Python3
URL:     http://github.com/miracle2k/flask-assets

Packager: Anton Midyukov <antohami@altlinux.org>

# Source-url: http://github.com/miracle2k/flask-assets/archive/refs/tags/%version.tar.gz
Source: %srcname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-webassets

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-flask
BuildRequires: python3-module-nose
BuildRequires: python3-module-yaml
%endif

BuildArch: noarch

%description
Integrates the webassets library with Flask, adding support
for merging, minifying and compiling CSS and Javascript files.

%prep
%setup -n %srcname-%version

%build
%python3_build

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v || :

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.rst

%changelog
* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 2.0-alt1
- Initial build for Sisyphus
