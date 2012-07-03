%define _kde4_alternate_placement 1

Name:		plasma-applet-todolist
Version:	0.4
Release:	alt1

Summary:	Todo List plasmoid using akonadi
License:        GPLv2
Group:          Graphical desktop/KDE
URL:            http://www.kde-look.org/content/show.php/todo+list?content=90706
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	90706-todo_plasmoid-0.4.tar.bz
Patch0:		plasma-applet-todolist-0.4-mdv-fix-category.patch

BuildRequires(pre): kde4libs-devel
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	kde4pimlibs-devel
BuildRequires:	akonadi-devel

%description
Plasmoid that shows KOrganizer 'todo' list using akonadi.

%prep
%setup -q -n todo_plasmoid
%patch0 -p0

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc README COPYING AUTHORS
%_K4lib/*.so
%_K4srv/*.desktop

%changelog
* Sun Feb 06 2011 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- Initial build in Sisyphus (closes: #23130)

