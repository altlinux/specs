# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(HTML/Entities.pm)
# END SourceDeps(oneline)

Name:    xsr
Version: 1.0.0.0.126.git6c87ad2
Release: alt1

Summary: Program that make a recording of all the steps
License: MIT
Group:   Graphical desktop/Other
Url:     https://github.com/nonnymoose/xsr

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

Requires: scrot
Requires: xinput
Requires: xdotool
Requires: ImageMagick-tools

%description
Program that allows users to make a recording of all of the steps they took.
(It's like a screen recorder except it doesn't record a video.)

It records your keystrokes, and it saves the output as standard html
(base64-uri-encoded images) rather than mhtml.
This allows for easy editing of the resultant file, such as to remove passwords
you typed.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -m644 Cursor.png %buildroot%_datadir/%name
install -m644 {xsr.css,xsr-min.css} %buildroot%_datadir/%name
install -Dm755 %name %buildroot%_bindir/%name

%files
%doc *.md LICENSE
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*.css
%_datadir/%name/*.png

%changelog
* Tue Mar 26 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0.0.0.126.git6c87ad2-alt1
- Initial build for Sisyphus (Closes: #49766)
