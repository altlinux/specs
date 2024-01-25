%define        oname AlembicEntity
%define        _name alembic

Name:          qml-%{_name}
Version:       2023.2.0
Release:       alt1
Summary:       Qml Alembic plugin to visualize Alembic Point Clouds
License:       MPL-2.0
Group:         Sciences/Mathematics
Url:           https://github.com/alicevision/qmlAlembic
Vcs:           https://github.com/alicevision/qmlAlembic.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         config.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-3d-devel
#BuildRequires: ilmbase-devel
BuildRequires: alembic-devel
BuildRequires: imath-devel

%description
qmlAlembic is a C++ QML plugin providing classes to load and visualize Alembic
point cloud files in Qt3D. It has been developed to load AliceVision sparse
reconstruction results inside Meshroom.


%prep
%setup
%patch

%build
%cmake -DQML_INSTALL_DIR=%_qt5_qmldir/
%cmake_build

%install
%cmakeinstall_std


%files
%doc README*
%_qt5_qmldir/%{oname}/


%changelog
* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 2023.2.0-alt1
- initial build for Sisyphus
