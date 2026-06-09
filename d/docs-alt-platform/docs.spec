%define variant alt-platform
%define Variant ALT Platform

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

Name: docs-%variant
Version: 11.0
Release: alt2

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Obsoletes: docs-basealt-desktop <= 8.0-alt2

BuildRequires(pre): rpm-macros-alternatives
BuildRequires(pre): rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

# Set alternative to doc
mkdir -p -- %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_documentationdir	%_docsinstalldir	63
EOF

%files
%_docsinstalldir
%_altdir/%name

%changelog
* Tue Jun 09 2026 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- fix some typos (ALT 59449, 59448, 59447)
- fix crane (ALT 59455, 59457, 59454, 59453)
- fix trivy (ALT 59458)
- fix regctl (ALT 59452, 59451)
- small improvements (ALT 59450)

*Thu May 14 2026 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- initial build
