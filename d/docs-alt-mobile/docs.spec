%define variant alt-mobile
%define Variant ALT Mobile

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

Name: docs-%variant
Version: 11.0
Release: alt4

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
%_documentationdir	%_docsinstalldir	61
EOF

%files
%_docsinstalldir
%_altdir/%name

%changelog
* Fri Mar 13 2026 Elena Mishina <lepata@altlinux.org> 11.0-alt4
- update to ALT Mobile 11.0RC3

* Mon Jan 19 2026 Elena Mishina <lepata@altlinux.org> 11.0-alt3
- small improvements
- typo fixes (closes #57525)

* Tue Dec 30 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt2
- update to ALT Mobile 11.0RC1
- small improvements (closes #57194, #57196)
- typo fixes (closes #57186, #57195)

* Wed Nov 19 2025 Elena Mishina <lepata@altlinux.org> 11.0-alt1
- initial build
