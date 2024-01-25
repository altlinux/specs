Name:          cmake-library
Version:       20230519
Release:       alt1
Summary:       CI and VCI cmake macros
License:       Unlicenced
Group:         Development/C
Url:           https://gitlab.vci.rwth-aachen.de:9000/cmake/cmake-library
Vcs:           https://gitlab.vci.rwth-aachen.de:9000/cmake/cmake-library.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar

Requires:      cmake

%description
CI and VCI cmake macros.


%prep
%setup

%install
mkdir -p %buildroot%_libdir/cmake/ %buildroot%_datadir/cmake/Modules/
cp -r CI VCI %buildroot%_libdir/cmake/
cp finders/* %buildroot%_datadir/cmake/Modules/

%files
%doc README*
%_libdir/cmake/
%_datadir/cmake/Modules/

%changelog
* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 20230519-alt1
- initial build for Sisyphus
