# e60401278f8933211eaac168475a3c332d62531c

%define module_name sleekxmpp
%def_with python3

Name: python-module-%module_name
Version: 1.2.0
Release: alt0.1.gite6040127
Summary: Flexible XMPP client/component/server library for Python

License: MIT
Group: Development/Python
URL: https://github.com/fritzy/SleekXMPP

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-distribute
Requires: python-module-pyasn1 python-module-pyasn1-modules python-module-dns
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute 
%endif

%description
SleekXMPP is a flexible XMPP library for python that allows
you to create clients, components or servers for the XMPP protocol.
Plug-ins can be create to cover every current or future XEP.


%package -n python3-module-%module_name
Summary: Flexible XMPP client/component/server library for Python
Group: Development/Python3
Requires: python3-module-pyasn1 python3-module-pyasn1-modules python3-module-dns
%add_python3_req_skip UserDict

%description -n python3-module-%module_name
SleekXMPP is a flexible XMPP library for python that allows
you to create clients, components or servers for the XMPP protocol.
Plug-ins can be create to cover every current or future XEP.


%prep
%setup -q

%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc LICENSE README.rst
%python_sitelibdir/%module_name
%exclude %python_sitelibdir/*.egg-*

%files -n python3-module-%module_name
%doc LICENSE README.rst
%python3_sitelibdir/%module_name
%exclude %python3_sitelibdir/*.egg-*

%changelog
* Tue Sep 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.1.gite6040127
- initial build
- git snapshot e60401278f8933211eaac168475a3c332d62531c
