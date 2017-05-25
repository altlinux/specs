%define modulename telebot
%def_with python3

Name: python-module-%modulename
Version: 3.0.0
Release: alt1

%setup_python_module %modulename

Summary: Python Telegram bot api
License: GPL2
Group: Development/Python

Url: https://github.com/eternnoir/pyTelegramBotAPI
Packager: Konstantin Artyushkin <akv@altlinux.org>
BuildArch: noarch

Source: %modulename-%version.tar

#BuildPreReq: %py_dependencies setuptools
BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires: python3-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
%summary

#--------------------------------------------------------------------------------
%if_with python3
%package -n python3-module-%modulename
Summary: Python Telegram bot api
Group: Development/Python3

%description -n python3-module-%modulename
%summary
%endif
#--------------------------------------------------------------------------------

%prep
%setup -n %modulename-%version

%if_with python3
rm -fr ../python3
cp -a ./ ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

#--------------------------------------------------------------------------------
%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/pyTelegramBotAPI*.egg-info
%endif
#--------------------------------------------------------------------------------


%changelog
* Thu May 25 2017 Konstantin Artyushkin <akv@altlinux.org> 3.0.0-alt1
- initial build

