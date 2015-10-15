Name: python-module-websockify
Version: 0.6.1
Release: alt1
Summary: WSGI based adapter for the Websockets protocol
Group: Development/Python

License: LGPLv3
Url: https://github.com/kanaka/websockify
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

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

rm -Rf %buildroot/usr/share/websockify
mkdir -p %buildroot%_mandir/man1/
install -m 444 docs/websockify.1 %buildroot%_man1dir/

%files
%doc LICENSE.txt docs
%_man1dir/websockify.1*
%python_sitelibdir/*
%_bindir/websockify

%changelog
* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-2.fc21.src)

