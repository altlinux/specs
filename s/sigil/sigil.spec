Name: sigil
Version: 0.9.8
Release: alt1

%set_verify_elf_method unresolved=relaxed

Summary: Sigil is a free, open source, multi-platform WYSIWYG ebook editor
Summary(ru_RU.UTF-8): Sigil это свободный, открытый, многоплатформенный редактор типа WYSIWYG для электронных книг
License: GPLv3
Group: Editors
Url: https://sigil-ebook.com/

# skip dependencies which are actually provided (but files are located at non-standard location)
%add_python3_req_skip opf_newparser quickparser sigil_bs4 sigil_bs4.builder._lxml

# https://github.com/Sigil-Ebook/Sigil.git
Source: %name-%version.tar

Patch1: %name-%version-fedora-pluginrunner.patch
Patch2: %name-%version-fedora-system-dicts.patch
Patch3: %name-%version-alt-build.patch
Patch4: %name-%version-alt-dont-check-for-updates.patch
Patch5: %name-%version-alt-fix-version.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++ zlib-devel libhunspell-devel libpcre-devel
BuildRequires: qt5-base-devel qt5-webkit-devel qt5-svg-devel qt5-tools-devel qt5-xmlpatterns-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel boost-datetime-devel boost-regex-devel boost-thread-devel boost-system-devel
BuildRequires: python3-dev libminizip-devel

%description
Sigil is a free, open source, multi-platform WYSIWYG ebook editor.
It is designed to edit books in ePub format.

%description -l ru_RU.UTF-8
Sigil это свободный, открытый, многоплатформенный редактор
типа WYSIWYG для электронных книг.
Он разработан для правки книг в формате ePub.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%cmake \
	-DUSE_SYSTEM_LIBS:BOOL=ON \
	-DSYSTEM_LIBS_REQUIRED:BOOL=ON

pushd BUILD
%make_build
popd

%install
pushd BUILD
%makeinstall_std
popd

mkdir -p %buildroot%_liconsdir
mv %buildroot%_pixmapsdir/*.png %buildroot%_liconsdir/

%files
%doc README.md ChangeLog.txt
%_bindir/*
%_libdir/%name
%_desktopdir/*.desktop
%_liconsdir/*.png
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri Sep 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.8-alt1
- Updated to upstream version 0.9.8.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.1-alt1.qa1
- NMU: rebuilt with rebuilt libFlightCrew.so.0.7.

* Mon Dec 03 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.1-alt1
- new version

* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- Imported version sigil 0.4

* Sat Feb 19 2011 Malo Skryleve <malo@altlinux.org> 0.3.4-alt1
- initial build for ALT Linux Sisyphus

