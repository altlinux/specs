%define _unpackaged_files_terminate_build 1

Name: sigviewer
Version: 0.6.4
Release: alt5.git.f62f8d9
Summary: SigViewer is a viewing application for biosignals
Group: Sciences/Medicine
License: GPL-3.0+
Url: https://github.com/cbrnr/sigviewer

# https://github.com/cbrnr/sigviewer.git
Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: biosig-devel libxdf-devel

%description
SigViewer is a viewing application for biosignals such as EEG or MEG time series.
In addition to viewing raw data, SigViewer can also create, edit,
and display event information (such as annotations or artifact selections).

%prep
%setup
%patch1 -p1

%build
%qmake_qt5 \
	CONFIG+=nostrip \
	%nil

%make_build

# compile translations
if stat src/translations/*.ts 2>/dev/null 1>&2 ; then
	for i in src/translations/*.ts ; do
		lrelease-qt5 $i -qm ${i%%.ts}.qm
	done
fi

%install
install -Dpm755 bin/release/%name %buildroot%_bindir/%name
install -Dpm644 %{name}.svg %buildroot%_pixmapsdir/%{name}.svg
install -Dpm644 deploy/debian/%{name}128.png %buildroot%_pixmapsdir/%{name}128.png
install -Dpm644 deploy/debian/%{name}.desktop %buildroot%_desktopdir/%{name}.desktop

# install translations
if stat src/translations/*.qm 2>/dev/null 1>&2 ; then
	install -d %buildroot%_qt5_translationdir
	for i in src/translations/*.qm ; do
		install -Dpm644 $i %buildroot%_qt5_translationdir/$(basename "$i")
	done
fi

%find_lang --with-qt %name

%files -f %name.lang
%doc LICENSE
%doc README.md
%_bindir/%name
%_pixmapsdir/%{name}128.png
%_pixmapsdir/%{name}.svg
%_desktopdir/%{name}.desktop

%changelog
* Tue Sep 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt5.git.f62f8d9
- Fixed typo in translation.

* Tue Sep 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt4.git.f62f8d9
- Added translation by Sergey Kazorin.
- Fixed issues related to translation.

* Mon Aug 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt3.git.f62f8d9
- Installed and enabled translations.

* Mon Aug 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt2.git.f62f8d9
- Fixed crashes in Power Spectrum tool.

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt1.git.f62f8d9
- Initial build for ALT.
