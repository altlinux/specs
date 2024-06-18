%define basic_name control++gui
%define controlpp_intf %{python3_sitelibdir_noarch}/controlpp_intf
%define controlppgui_widgets %{python3_sitelibdir_noarch}/controlppgui_widgets
%define thisdocdir %{_defaultdocdir}/%{name}

Name: python3-module-%{basic_name}
Version: 0.2.0
Release: alt1

Summary: GUI for the glorious control++ app
License: GPLv3
Group: System/Configuration/Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/python3-module-controlplusplus.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-kivy
Requires: python3
Requires: python3-module-kivy
Requires: control++ >= 0.24

%description
Graphical interface for control++ that uses kivy framework.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{controlpp_intf}
mkdir -p %{buildroot}%{controlppgui_widgets}
mkdir -p %{buildroot}%{thisdocdir}
# Executable and kv-file
cp %{basic_name} %{buildroot}%{_bindir}
cp controlppgui.kv %{buildroot}%{_bindir}
# Modules
cp controlpp_intf/*.py %{buildroot}%{controlpp_intf}
cp controlppgui_widgets/*.py %{buildroot}%{controlppgui_widgets}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{_bindir}/%{basic_name}
%{_bindir}/controlppgui.kv
%{controlpp_intf}
%{controlppgui_widgets}
%{thisdocdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Tue Jun 18 2024 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Fix of a bug that manifested when there were active macro and micro modes
  at the same time;
- Date and time of activation of the modes are displayed in the mode selection
  table.

* Sun May 12 2024 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
