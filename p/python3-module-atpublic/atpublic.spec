%define _unpackaged_files_terminate_build 1
%define oname atpublic

Name: python3-module-%oname
Version: 1.0
Release: alt1

Summary: Simple decorator and function which populates a module's __all__.
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/atpublic
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel


%description
This is a very simple decorator and function which populates a module's __all__
and optionally the module globals. This provides both a pure-Python 
implementation and an optional C implementation.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.* README.*
%python3_sitelibdir/*


%changelog
* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
