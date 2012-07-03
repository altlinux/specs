%define fname theano

Name: fonts-ttf-%fname
Version: 2.0
Release: alt1

Summary: Theano Classical TrueType Fonts

License: SIL OFL
Group: System/Fonts/True type
Url: http://www.thessalonica.org.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.thessalonica.org.ru/downloads/%fname-%version.ttf.zip

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
Theano is a common name for some fonts I have designed from historic
samples. Most of these fonts were initially intended as Greek-only
faces, but finally I found it interesting to supplement them with
stylistically compatible Latin letters, thus reproducing the general
look of old classical text editions. For this reason Theano fonts currently
have no additional weights or styles and don't provide extensive Unicode
coverage: just a standard set of Latin and Greek characters (including
the full polytonic set) and some additional characters I found interesting
to design. Nevertheless I decided to make them publicly available in the
hope they can be useful for other classicists or medievalists.

The package is named after Theano, a famous Ancient Greek woman
philosopher, who was first a student of Pythagoras, and supposedly became
his wife. In 1211 or 1212 Michael Choniates, a highly educated Greek
Metropolitan of Athens, wrote a large poem devoted to Theano. Thus Theano
seemed a good example of a person joining the ancient and the medieval world.
Another reason for which I selected her name is that it starts from
theta, just like Thessalonica -- the name of my keyboard input and conversion 
utility for Ancient Greek.

Designed by Alexey Krukov.

%prep
%setup -c %name

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc OFL*.txt FONTLOG.txt

%changelog
* Mon Jun 13 2011 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- NMU: 2.0 (30.04.2011)
- use original zip file as a source archive

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
