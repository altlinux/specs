%define _unpackaged_files_terminate_build 1

Name: files-indicator
Version: 0.1.0
Release: alt1

Summary: Indicator for easy access to recent files and folders
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/SergKolo/files-indicator

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

Requires: typelib(AyatanaAppIndicator3)
Requires: typelib(Notify)
Requires: typelib(GdkPixbuf)
%filter_from_requires /^python3(gi.repository.GdkPixbuf)/d

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Indicator for easy access to recent files and folders

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
mkdir -p %{buildroot}%{_bindir}
cp -pv files-indicator %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_desktopdir}
cp -pv files-indicator.desktop %{buildroot}%{_desktopdir}/

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop

%changelog
* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
