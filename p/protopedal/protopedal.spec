Name:    protopedal
Version: 2.5
Release: alt1

Summary: Compatibility tool for sim racing pedals and force feedback steering wheels
License: EUPL-1.2
Group:   System/Configuration/Hardware
Url:     https://gitlab.com/openirseny/protopedal/
VCS:     https://gitlab.com/openirseny/protopedal.git

Source: %name-%version.tar

BuildRequires: gcc-c++

ExclusiveArch: x86_64

%description
Compatibility tool for sim racing pedals and force feedback steering wheels.
Helps with wheel and pedal detection by creating virtual devices with
extended capabilities. Facilitates merging devices, range adjustments,
custom curves, button to axis and axis to button mappings.

%prep
%setup

%build
export CFLAGS="%optflags"
export CXXFLAGS="${CFLAGS}"

%make_build

%install
install -D -m755 protopedal %buildroot%_bindir/protopedal

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Mon Feb 24 2025 Sergey Palcheh <minergenon@altlinux.org> 2.5-alt1
- initial build for ALT Sisyphus

