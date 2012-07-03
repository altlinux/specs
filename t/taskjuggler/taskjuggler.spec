Name:          taskjuggler
Version:       2.4.3
Release:       alt1
Summary:       Project management tool

Group:         Office
License:       GPLv2
URL:           http://www.taskjuggler.org
Source0:       http://www.taskjuggler.org/download/%{name}-%{version}.tar.bz2
Source1:       %{name}.xml

BuildRequires(pre): rpm-macros-kde-common-devel
BuildRequires: gcc-c++
BuildRequires: kdepim-devel libqt3-devel libjpeg-devel
Buildrequires: xmlto libical-devel

%description
TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects
and scales easily to projects with hundreds of resources and thousands of
tasks. It covers the complete spectrum of project management tasks from the
first idea to the completion of the project. It assists you during project
scoping, resource assignment, cost and revenue planning, and risk and
communication management.

%prep
%setup -q
#/foo/bar timezone is completely valid and interpreted as UTC,skipping test
rm -f TestSuite/Syntax/Errors/Timezone.tjp


%build
%add_optflags -I%_includedir/tqtinterface
%K3configure --with-kde-support=yes --libdir=%_K3lib
%make_build

#generate manpages with xmlto
xmlto man --skip-validation man/en/taskjuggler.xml
xmlto man --skip-validation man/en/TaskJugglerUI.xml


%install
%K3install

mkdir -p %buildroot%_mandir/man1
cp -p *.1 %buildroot%_mandir/man1
rm %buildroot%_K3lib/libtaskjuggler.{la,so}

# install mime type definition
install %SOURCE1 -Dpm 644 %buildroot%_K3xdg_mime/%name.xml

%K3find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README TODO
%_K3bindir/TaskJugglerUI
%_K3bindir/taskjuggler
%_K3lib/libtaskjuggler.*
%_K3xdg_apps/*.desktop
%_K3apps/katepart/syntax/%name.xml
%_K3apps/%name/
%_K3conf/taskjugglerrc
%_K3mimelnk/application/*.desktop
%_K3xdg_mime/%name.xml
%_kde3_iconsdir/hicolor/*/apps/%name.png
%_datadir/icons/crystalsvg/*/mimetypes/*.png
%_mandir/man1/*

%changelog
* Sat Mar 05 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Return to Sisyphus

