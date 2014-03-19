
Name:           kdesvn
Version:        1.6.0
Release:        alt1
Summary:        A subversion client for KDE4 with KIO integration

Group:          Development/Tools
License:        GPLv2+
URL:            https://projects.kde.org/projects/playground/devtools/kdesvn
# git clone git://anongit.kde.org/kdesvn
Source0:        %name-%{version}.tar

BuildRequires(pre): kde4libs-devel
BuildRequires:  gcc-c++
BuildRequires:  subversion-devel

%description
KDESvn is a frontend to the subversion vcs. In difference to most other
tools it uses the subversion C-Api direct via a c++ wrapper made by
Rapid SVN and doesn't parse the output of the subversion client. So it
is a real client itself instead of a frontend to the command line tool.

It is designed for the K-Desktop environment and uses all of the goodies
it has. It is planned for future that based on the native client some
plugins for konqueror and/or kate will made.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use the %{name} subversion wrapper library.

%prep
%setup -q

%build
%K4build
 
%install
%K4install
%K4find_lang --with-kde %name

#Don't conflict with kdesdk
rm %buildroot%_K4srv/svn*.protocol

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING GPL.txt TODO
%_bindir/kdesvn*
%_K4libdir/libsvnqt.so.*
%_K4lib/*.so
%_K4srv/*
%_K4conf_update/*
%_K4apps/kdesvn/*
%_K4apps/kdesvnpart/*
%_K4cfg/*.kcfg
%_K4dbus_interfaces/*.xml
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svgz
%_datadir/svnqt
%_desktopdir/kde4/*.desktop
%doc %_K4doc/*
%doc %_man1dir/kdesvn*.1*


%files devel
%_K4link/libsvnqt.so
%_includedir/svnqt

%changelog
* Wed Mar 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- First build KDE4 version for ALT Linux (ALT #29251)
