%define        _gimpscriptsdir %(gimptool-3 --gimpdatadir)/scripts/

Name:          gimp-plugin-watermark
Version:       20230103
Release:       alt2.1
Summary:       Watermark GIMP scripts
License:       Unlicense
Group:         Graphics
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires: libgimp-devel

%description
Watermark GIMP scripts.


%prep
%setup

%build

%install
install -D -t %buildroot/%_gimpscriptsdir -m644 *.scm


%files
%_gimpscriptsdir/*


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 20230103-alt2.1
- ![FTBFS] fixed call to gimptool-3

* Thu Mar 20 2025 Constantin Sunzow <protvin@altlinux.org> 20230103-alt2
- Fix FTBFS: use gimptool-3.0 instead gimptool-2.0.

* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 20230103-alt1
- initial build for Sisyphus
