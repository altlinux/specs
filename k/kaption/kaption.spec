%define  kdeapp 139302

Name:    kaption
Version: 0.1.1
Release: alt1
Summary: A KDE utility similar to Jing or Skitch not yet as powerful as them

License: GPLv2+
Group:   Graphics
URL:     http://kde-apps.org/content/show.php/?content=%{kdeapp}

Source:  http://kde-apps.org/CONTENT/content-files/%kdeapp-%name-%version.tar.bz2

BuildRequires(pre): kde4libs-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
It's an app that sit in the systray, left clicking the icon you can
capture a screen region to draw arrows, boxes and text on it, than you
can save the result (the screenshots shown here are made with this app).

This program has the following features:
* Screen capture
* Ability to draw arrows, boxes, ellipses and text on the captured region
* Ability to choose color, size and font of your drawings
* FTP/SFTP Upload


%prep
%setup -q -n %name-%version

%build
%K4build -DCMAKE_SKIP_RPATH=1

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS COPYING INSTALL README TODO
%_bindir/*
%_K4datadir/apps/*
%_K4xdg_apps/*
%_K4cfg/*


%changelog
* Mon Oct 08 2012 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Initial build in Sisyphus

