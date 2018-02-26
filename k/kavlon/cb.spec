%define srcname cb

Name: kavlon
Version: 0.13
Release: alt2
Summary: A simple coloring book program written in Python.
Group: Graphics

License: GPL

Source0: %srcname-%version.tar.gz
Source1: %name-run-script
Patch0: %name-0.13-alt-config-fps.patch
Patch1: %name-0.13-alt-image-name.patch

#add_python_req_skip py2exe
# from windist.py

BuildRequires: python-devel
BuildArch: noarch

%description
Kavlon Coloring Book is a simple coloring book program written in Python
with Pygame.

%prep
%setup -q -n %srcname
%patch0 -p1
%patch1 -p2

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_bindir
rm -f windist.py
cp -r * %buildroot%_libexecdir/%name
install -m755 %SOURCE1 %buildroot%_bindir/%name


%files
%_libexecdir/%name
%_bindir/%name


%changelog
* Wed Oct 26 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13-alt2
- add image name patch
- remove windist.py

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1.1
- Rebuild with Python-2.7

* Tue Sep 28 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13-alt1
- Initial

