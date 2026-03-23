%define variant alt-domain
%define Variant ALT Domain

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

Name: docs-%variant
Version: 11.1
Release: alt3

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

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
%_documentationdir	%_docsinstalldir	54
EOF

%files
%_docsinstalldir
%_altdir/%name

%changelog
* Fri Jan 30 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt3
- add alt-services
- add LAPS
- fix typos (closes #57773, #57768)

* Fri Jan 30 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt2
- the spec file has been rewritten to support alternatives
- add new GNOME admx file (closes #57406)

* Mon Jan 26 2026 Elena Mishina <lepata@altlinux.org> 11.1-alt1
- add: laps, alt-services
- fix typos (closes #57404)

* Thu Nov 27 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt3
- fix dhcp script (closes #56174)
- fix sssd settings (closes #56177)
- update: ADMC
- add: gMSA, usershares, troubleshooting

* Fri Sep 26 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- fix typos (closes #56055, #56054, #56053, #56052, #56051, #56162, #56179)
- small improvements (closes #56164, #56165, #56166, #56167, #56176)
- fix command samba-tool (#56163, #56170, #56171, #56172 #56175)

* Fri Aug 22 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- initial build for Sisyphus
