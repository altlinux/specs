%define basic_name control++gui
%define controlpp_intf %{python3_sitelibdir_noarch}/controlpp_intf
%define controlppgui_kv %{_target_libdir_noarch}/controlppgui
%define controlppgui_widgets %{python3_sitelibdir_noarch}/controlppgui_widgets
%define thisdocdir %{_defaultdocdir}/%{name}

%define what_this_package_is_about Graphical user interface for the control++ \
application using the kivy framework.

Name: python3-module-%{basic_name}
Version: 0.2.0
Release: alt2

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
%what_this_package_is_about

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %basic_name
Summary: %summary
Group: %group
Requires: %name = %EVR

%description -n %basic_name
%what_this_package_is_about

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{controlpp_intf}
mkdir -p %{buildroot}%{controlppgui_kv}
mkdir -p %{buildroot}%{controlppgui_widgets}
mkdir -p %{buildroot}%{thisdocdir}
# Executable
cp %{basic_name} %{buildroot}%{_bindir}
# Modules and the kv-file
cp controlpp_intf/*.py %{buildroot}%{controlpp_intf}
cp controlppgui.kv %{buildroot}%{controlppgui_kv}
cp controlppgui_widgets/*.py %{buildroot}%{controlppgui_widgets}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{_bindir}/%{basic_name}
%{controlpp_intf}
%{controlppgui_kv}
%{controlppgui_widgets}
%{thisdocdir}

%files -n %{basic_name}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Wed Feb 12 2025 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt2
- The kv-file is moved to a more suitable location;
- The "control++gui" metapackage is added, which contains all the requirements
  for running the application.

* Tue Jun 18 2024 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Fix of a bug that manifested when there were active macro and micro modes
  at the same time;
- Date and time of activation of the modes are displayed in the mode selection
  table.

* Sun May 12 2024 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
