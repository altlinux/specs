Name: blender-docs
Version: 2.28.20030825
Release: alt2

Summary: Documentation for Blender
License: OPL
Group: Books/Other
Url: http://download.blender.org/documentation/

BuildArch: noarch
BuildRequires: docbook-utils

Packager: Alexandra Panyukova <mex3@altlinux.ru>

Source: %name-%version.tar.bz2

%description
Full documentation for Blender

%prep
%setup -q

%build
make html

%install
mkdir -p %buildroot%_defaultdocdir/%name
mv gfx html/
find html -type d -name CVS | xargs rm -rf
mv html %buildroot%_defaultdocdir/%name/
ln -s book1.html %buildroot%_defaultdocdir/%name/html/index.html

%files
%_defaultdocdir/%name

%changelog
* Wed Apr 02 2008 Panyukova Alexandra <mex3@altlinux.ru> 2.28.20030825-alt2
- bug #11574 fixed: symlink corrected
* Tue Nov 25 2003 Kachalov Anton <mouse@altlinux.ru> 2.28.20030825-alt1
- build for sisyphus
