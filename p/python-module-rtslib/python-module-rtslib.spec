%def_with python3

Name:           python-module-rtslib
License:        ASL 2.0
Group:          Development/Python
Summary:        API for Linux kernel LIO SCSI target
Version:        2.1.fb48
Release:        alt2
URL:            https://fedorahosted.org/targetcli-fb/
Source:         %{name}-%{version}.tar
Source1:        target.service
BuildArch:      noarch
BuildRequires:  python-devel python-module-epydoc python-module-setuptools python-module-json
Requires:       python-module-kmod

%if_with python3
BuildRequires:  rpm-build-python3 python3-module-setuptools
%endif

%package doc
Summary:        Documentation for python-rtslib
Group:          Documentation
Requires:       %{name} = %{version}-%{release}


%description
API for generic Linux SCSI kernel target. Includes the 'target'
service and targetctl tool for restoring configuration.

%description doc
API documentation for rtslib, to configure the generic Linux SCSI
multiprotocol kernel target.

%if_with python3
%package -n python3-module-rtslib
Summary:        API for Linux kernel LIO SCSI target
Group:          Development/Python

%description -n python3-module-rtslib
API for generic Linux SCSI kernel target.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
gzip --stdout doc/targetctl.8 > doc/targetctl.8.gz
gzip --stdout doc/saveconfig.json.5 > doc/saveconfig.json.5.gz
mkdir -p doc/html
epydoc --no-sourcecode --html -n rtslib -o doc/html rtslib/*.py

%if_with python3
pushd ../python3
2to3 --write --nobackups .
%python3_build
popd
%endif

%install
%python_install
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/target.service
install -m 644 doc/targetctl.8.* %{buildroot}%{_mandir}/man8/
install -m 644 doc/saveconfig.json.5.* %{buildroot}%{_mandir}/man5/

%if_with python3
pushd ../python3
# We don't want py3-converted scripts overwriting py2 scripts
# Shunt them elsewhere then delete
%python3_install --install-scripts py3scripts
rm -rf %{buildroot}/py3scripts
popd
%endif

%post
%post_service target

%preun
%preun_service target

%files
%{python_sitelibdir}/*
%{_bindir}/targetctl
%{_unitdir}/target.service
%doc COPYING README.md doc/getting_started.md
%{_mandir}/man8/targetctl.8.*
%{_mandir}/man5/saveconfig.json.5.*

%if_with python3
%files -n python3-module-rtslib
%{python3_sitelibdir}/*
%doc COPYING README.md
%endif

%files doc
%doc doc/html

%changelog
* Sun Jan 31 2016 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb48-alt2
- Man pages packaging fixed

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb48-alt1
- First build for ALT (based on Fedora 2.1.fb48-1.fc21.src)

