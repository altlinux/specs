Name:           wikipediafs
Version:        0.3
Release:        alt1.1
Summary:        View and edit Wikipedia articles as files
Packager:       Paul Wolneykien <manowar@altlinux.ru>

Group:          System/Kernel and hardware
License:        GPLv2
URL:            http://wikipediafs.sourceforge.net/

Source:        %{name}-%{version}.tar.gz

%py_package_requires fuse >= 0.2

BuildPreReq:    python-devel rpm-build-python python-module-fuse
BuildArch:      noarch

%description
WikipediaFS is a mountable Linux virtual file system that allows to
read and write articles from and to Wikipedia (or any Mediawiki-based
site) as files.

%prep
%setup

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --prefix %{_prefix} -O1 --skip-build \
                             --root %{buildroot}

%files
%doc AUTHORS COPYING README
%{python_sitelibdir}/%{name}
%{python_sitelibdir}/%{name}-*.egg-info
%{_bindir}/mount.%{name}
%{_man1dir}/mount.%{name}.1.gz

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Tue Dec 29 2009 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1
- Initial build for ALTLinux
