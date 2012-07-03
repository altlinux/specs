Version:	1.04.0.3532
Release:	alt1.qa2.1
License:	GPL
Group:		Development/Python
Summary:	eLearning XHTML editor
%setup_python_module exe
Name:		%packagename
Buildarch:	noarch
Source:		http://eduforge.org/frs/download.php/839/%modulename-%version-source.tgz
Packager: Fr. Br. George <george@altlinux.ru>

Requires: mimetex

# Automatically added by buildreq on Sat Aug 29 2009
BuildRequires: python-module-Nevow python-module-OpenSSL python-module-serial python-module-setuptools python-modules-encodings python-modules-logging
BuildRequires: desktop-file-utils

%description
Python module for eXe, eLearning XHTML editor

%package -n %modulename
License:	GPL
Summary:	Python module for eXe, eLearning XHTML editor
Buildarch:	noarch
Group:		Education

Requires:	%name = %version

%description -n %modulename
The eXe project is an authoring environment to enable teachers to publish web
content without the need to become proficient in HTML or XML markup.  Content
generated using eXe can be used by any Learning Management System.

%prep
%setup -n %modulename

%build
%python_build

%install
%python_install
rm -rf %buildroot%_datadir/%modulename/formless %buildroot%_datadir/%modulename/nevow %buildroot%_datadir/%modulename/twisted

rm -rf %buildroot%_datadir/%modulename/templates/*.cgi %buildroot%_datadir/%modulename/templates/*.exe
ln -s %_var/www/cgi-bin/mimetex.cgi %buildroot%_datadir/%modulename/templates/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Editor \
	--remove-category=Application \
	--add-category=TextEditor \
	%buildroot%_desktopdir/exe.desktop

%files -n %modulename
%dir %_datadir/%modulename
%_datadir/%modulename/*
%_desktopdir/%modulename.desktop
%_liconsdir/%modulename.png
%_bindir/%{modulename}*

# TODO some python files actually want %_datadir/%modulename to exist
%files
%python_sitelibdir/%modulename

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.04.0.3532-alt1.qa2.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.04.0.3532-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for exe

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.04.0.3532-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.04.0.3532-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for exe
  * postclean-05-filetriggers for spec file

* Sat Aug 29 2009 Fr. Br. George <george@altlinux.ru> 1.04.0.3532-alt1
- Initial build freom scratch

