# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name: sugar-read
Version: 106
Release: alt1_1
Summary: A document reader for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Read
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Read/Read-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: libevince-devel
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: python-devel
BuildRequires: sugar-toolkit-gtk3-devel

Requires: libevince
Requires: evince
Requires: gobject-introspection
Requires: python-module-BeautifulSoup
Requires: sugar-toolkit-gtk3
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
The Read activity allows the laptop to act as a book reader. It has a
simple interface, and will view many kinds of text and image-based book-
like materials. It will have particular strengths in handheld mode, with
extremely low power consumption and simple navigation controls.

Read can read PDF files, single-page TIFF files, and also read DJVU files.

%prep
%setup -q -n Read-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.sugar.ReadActivity

%files -f org.laptop.sugar.ReadActivity.lang
%doc COPYING AUTHORS
%{sugaractivitydir}/Read.activity/


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 106-alt1_1
- new version; import from fc18

