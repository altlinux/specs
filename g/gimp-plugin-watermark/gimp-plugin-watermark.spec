%define        gimpscriptsdir %(gimptool-2.0 --gimpdatadir)/scripts/

Name:          gimp-plugin-watermark
Version:       20230103
Release:       alt1
Summary:       Watermark GIMP scripts
License:       Unlicense
Group:         Graphics
BuildArch:     noarch
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires: libgimp-devel

%description
Watermark GIMP scripts.


%prep
%setup

%build

%install
install -D -t %buildroot/%gimpscriptsdir -m644 *.scm


%files
%gimpscriptsdir/*


%changelog
* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 20230103-alt1
- initial build for Sisyphus
