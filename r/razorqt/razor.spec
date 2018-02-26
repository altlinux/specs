Name:		razorqt
Version:	0.2
Release:	alt1
License:	GPL
Group:		Graphical desktop/Other
Summary:	Razor is a toolbox-like desktop-environment	
Vendor:		Christopher "VdoP" Regali <chris.vdop@googlemail.com>
URL:		http://razor-qt.sf.net
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source:		%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++, cmake, make, qt4-devel 
Requires:	%{name}-desktop, %{name}-panel, %{name}-session

%description
Razor is a toolbox-like desktop-environment. While trying to feature
everything a modern desktop has to offer (panel, session, desktop)
it lets the user choose what to use.

%package	resources
Summary:	RazorQt resources
Group:		System/Libraries

%description	resources
RazorQt resources

%package	desktop
Summary:	RazorQt desktop
Group:		Graphical desktop/Other
Requires:	%{name}-resources

%description	desktop
RazorQt desktop

%package	panel
Summary:	RazorQt panel
Group:		Graphical desktop/Other
Requires:	%{name}-resources

%description	panel
RazorQt panel

%package	session
Summary:	RazorQt session
Group:		Graphical desktop/Other
Requires:	%{name}-resources, openbox

%description	session
RazorQt session

%package	devel
Summary:	RazorQt development package
Group:		Development/KDE and QT

%description	devel
RazorQt development package

%prep
%setup -q -n %{name}
# hack
uic-qt4 librazorqt/razorqt/aboutdlg.ui > razorqt-panel/src/ui_aboutdlg.h

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release
make
popd

%install
pushd build
%{makeinstall} DESTDIR=%{buildroot}
popd

%files

%files	resources
%_libdir/lib%name.so.*
%dir %_datadir/razor
%_datadir/razor/

%files	desktop
%_bindir/razor-desktop

%files	panel
%_bindir/razor-panel
%dir %_libdir/razor-panel
%_libdir/razor-panel/

%files	session
%_bindir/razor-session
%_datadir/xsessions/razor.desktop

%files	devel
%_libdir/lib%name.so
%dir %_includedir/%name
%_includedir/%name/

%changelog
* Thu Jan 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build to Sisyphus

* Thu Jan 06 2011 TI_Eugene <ti.eugene@gmail.com> 0.2-190
- Next build

* Wed Mar 04 2009 TI_Eugene <ti.eugene@gmail.com> 0.1
- Initital build in OBS
