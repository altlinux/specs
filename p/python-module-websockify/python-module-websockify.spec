Name:           python-module-websockify
Version:        0.5.1
Release:        alt1
Summary:        WSGI based adapter for the Websockets protocol
Group:		Development/Python

License:        LGPLv3
URL:            https://github.com/kanaka/websockify
Source0:        %{name}-%{version}.tar
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools

Requires:       python-module-setuptools

%description
Python WSGI based adapter for the Websockets protocol

%prep
%setup

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%python_build


%install
%python_install

rm -Rf %{buildroot}/usr/share/websockify
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/


%files
%doc LICENSE.txt docs
%{_mandir}/man1/websockify.1*
%{python_sitelibdir}/websockify/*
%{python_sitelibdir}/websockify-%{version}-py?.?.egg-info
%{_bindir}/websockify


%changelog
* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-2.fc21.src)

