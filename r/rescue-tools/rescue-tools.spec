Name: rescue-tools
Version: 1.0
Release: alt1

Summary: Scripts for create deploy USB/HDD sticks
License: GPL-3
Group: File tools

Url: http://www.altlinux.org/Rescue/Tools
Source: %name-%version.tar
BuildArch: noarch
AutoReq: yes, noshell

Packager: Leonid Krivoshein <klark@altlinux.org>

%description
Scripts for creation rescue/deploy USB-sticks, for change
boot methods in official ALT Linux ISO-9660, for launch
jobs inside ALT Rescue, for ALT Rescue self-testing.

%prep
%setup
chmod -- 0755 examples/autorun

%install
mkdir -pm755 %{buildroot}%_bindir
for tool in qemu-rescue rescue2stick; do
	cat $tool.in |sed -E 's,\{VERSION\},%version,g' \
			> "%{buildroot}%_bindir/$tool"
	chmod -- 0755 "%{buildroot}%_bindir/$tool"
done

%files
%_bindir/*
%doc examples

%changelog
* Wed Jul 29 2020 Leonid Krivoshein <klark@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

