Group: Engineering
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           3dprinter-udev-rules
Version:        0.3
Release:        alt1_2
Summary:        Rules for udev to give regular users access to operate 3D printers
License:        MIT-0
URL:            https://github.com/hroncok/%{name}
Source0:        https://github.com/hroncok/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch

# For the %%_udevrulesdir macro
BuildRequires:  libsystemd-devel libudev-devel systemd

# For the directory
Requires:        udev

%global file_name 66-3dprinter.rules
Source44: import.info

%description
Normally, when you connect a RepRap like 3D printer to a Linux machine by an
USB cable, you need to be in dialout or similar group to be able to control
it via OctoPrint, Printrun, Cura or any other control software. Not any more.

Install this rule to grant all users read and write access to collected
devices based on the VID and PID.

Disclaimer: Such device might not be a 3D printer, it my be an Arduino, it
might be a modem and it might even be a blender. But normally you would
add your user to dialout and get access to all of those and more anyway.
So I guess be careful when some of the users should not get access to
your blenders.

%prep
%setup -q

%build
# nothing

%install
install -D -p -m 644 %{file_name} %{buildroot}%_udevrulesdir/%{file_name}

%files
%doc README.md
%doc --no-dereference LICENSE
%_udevrulesdir/%{file_name}

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.3-alt1_2
- update to new release by fcimport

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- cleaned up reauires (closes: #36631)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_2
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1
- update to new release by fcimport

* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_2
- converted for ALT Linux by srpmconvert tools

