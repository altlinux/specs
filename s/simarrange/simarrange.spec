%global commit d52382feb716621f9ac08d25a502420fc1d3c983
%global shortcommit d52382f
%global datestamp 20131019
%global relstring %{datestamp}git%{shortcommit}

Name:           simarrange
Version:        0.0
Release:        alt1.%{relstring}
Summary:        STL 2D plate packer with collision simulation

Group:		Engineering
License:        AGPLv3+
URL:            https://github.com/kliment/%name
Source0:        %{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  libadmesh-devel
BuildRequires:  libgomp-devel
BuildRequires:  libargtable2-devel
BuildRequires:  libopencv-devel
BuildRequires:  libuthash-devel

%description
Simarrange is a program that simulates collisions between STL meshes in 2D in
order to generate tightly packed sets of parts. It takes a directory of STL
files as input and outputs STL files with combined plates of parts.
The parts are assumed to be in the correct printable orientation already.

%prep
%setup -q -n %name-%commit

# bundling
rm utlist.h
rm admesh -rf

%build
# the build script is one line and would need patching, so just skip it
gcc %{optflags} simarrange.c -o ./%{name} -lm -lopencv_imgproc -lopencv_core \
    -lopencv_highgui -ladmesh -largtable2 -fopenmp -DPARALLEL

%install
install -Dpm0755 %name %buildroot%_bindir/%name
install -Dpm0644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc COPYING Readme
%_bindir/%name
%doc %_man1dir/%name.*

%changelog
* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.0-alt1.20131019gitd52382f
- Import from Fedora
