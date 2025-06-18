%define modulename nevow

Name: python3-module-%modulename
Version: 0.14.5
Release: alt1.20250324.1

Summary: Web Application Construction Kit
License: MIT
Group: Development/Python3

Url: https://github.com/beremiz/nevow-py3
VCS: https://github.com/beremiz/nevow-py3.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -r %buildroot/%_prefix/doc

%files
%_bindir/nevow-xmlgettext
%_bindir/nit
%python3_sitelibdir/nevow-%version.dist-info/
%python3_sitelibdir/nevow/
%exclude %python3_sitelibdir/nevow/test
%python3_sitelibdir/formless/
%python3_sitelibdir/twisted/plugins/*.py
%python3_sitelibdir/twisted/plugins/__pycache__/nevow_widget.cpython-*.pyc

%changelog
* Tue Jun 17 2025 Anton Midyukov <antohami@altlinux.org> 0.14.5-alt1.20250324.1
- Initial build.
