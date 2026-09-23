Name:    lovr-playspace
Version: 0.2.1
Release: alt1

Summary: Room boundary overlay for OpenXR
License: MIT
Group:   Graphics
URL:     https://github.com/SpookySkeletons/lovr-playspace

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Source2: lovr-playspace.sh

Requires: lovr

ExclusiveArch: x86_64

%description
LOVR Playspace is a room boundary overlay for OpenXR, made with LOVR.

Avoid bumping into walls! LOVR Playspace works on any OpenXR runtime that
implements EXTX_overlay - currently this is limited to Monado-based runtimes.

%prep
%setup -a1

%install
install -d %buildroot%_bindir
install -m0755 %SOURCE2 %buildroot%_bindir/lovr-playspace
install -d %buildroot%_datadir/%name/json
install -m0644 main.lua conf.lua %buildroot%_datadir/%name/
install -m0644 json/json.lua json/LICENSE %buildroot%_datadir/%name/json/

%files
%doc LICENSE README.md
%_bindir/lovr-playspace
%_datadir/%name

%changelog
* Wed Sep 23 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus
