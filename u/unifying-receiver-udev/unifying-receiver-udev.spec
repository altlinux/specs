Name:           unifying-receiver-udev
Version:        0.2
Release:        alt1

Group:          System/Configuration/Hardware
Summary:        udev rules for user access to Logitech Unifying Receiver
License:        GPLv3
URL:            http://www.brouhaha.com/~eric/software/%{name}/
Source0:        http://www.brouhaha.com/~eric/software/%{name}/download/%{name}-%{version}.tar.gz
BuildArch:      noarch

%global udev_order 69
%global udev_rules_dir /usr/lib/udev/rules.d

%description
Udev rules to allow user access to the Logitech Unifying Receiver, e.g.,
for use with ltunify, pairing_tool, or Solaar.

%prep
%setup -q

%build

%install
install -D -p -m 644 unifying-receiver.rules %buildroot%_udevrulesdir/%{udev_order}-unifying-receiver.rules

%files
%doc COPYING
%_udevrulesdir/*

%changelog
* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Import to Sisyphus from Fedora
