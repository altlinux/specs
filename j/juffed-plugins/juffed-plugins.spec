Name:		juffed-plugins
Summary:	Plugins for JuffEd text editor
Version:	0.8.1
Release:	alt5
License:	GPL
Group:		Editors	
URL:		http://code.google.com/p/juffed-plugins
Vendor:		Mikhail Murzin <mezomish@gmail.com>
Packager:	Andrey Cherepanov <cas@altlinux.org>	

Source:		%{name}_%{version}.tar.gz
Patch0:		use-external-qtermwidget.patch	

BuildRequires:	gcc-c++, libqt4-devel
BuildRequires: 	juffed-devel
BuildRequires: 	libqtermwidget-devel
Requires:	juffed

%description
%{summary}

%prep
%setup -q
%patch0 -p2
for f in `find . -type f -name \*.pro`; do 
subst "s,/share/juffed/plugins,/%_lib/juffed/plugins,g" $f
echo 'QMAKE_CXXFLAGS += %optflags' >> $f
done
DESTDIR=%buildroot PREFIX=/usr qmake-qt4 %name.pro

%build
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%_libdir/juffed/plugins/*.so*

%changelog
* Wed Mar 21 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt5
- Consider %%optflags (thanks sbolshakov@)

* Mon Jul 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt4
- Rebuild for new qscintilla2

* Tue Jan 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt3
- Rebuild with QTermWidget 0.2.0

* Mon Jan 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt2
- use external QTermWidget widget

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Initial build in Sisyphus

