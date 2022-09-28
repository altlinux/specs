Group: Graphical desktop/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}


Name:           brise
Version:        0.38.20180515
Release:        alt1_9
Summary:        The official Rime schema repository

License:        GPLv3
URL:            https://rime.im/
Source0:        https://github.com/rime/brise/releases/download/brise-0.38/%{name}-%{version}.tar.gz

BuildRequires:  librime-tools
Source44: import.info
BuildArch: noarch


%description
La brise: The official Rime schema repository.

%prep
%setup -q -n %{name}


%build
%make_build


%install
%makeinstall_std


%files
%doc README.md LICENSE ChangeLog AUTHORS
%{_datadir}/rime-data


%changelog
* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 0.38.20180515-alt1_9
- new version

