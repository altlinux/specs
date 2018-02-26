%define gimpver 2.0

Name: gimp-plugin-metadata
Version: 1.0
Release: alt1

Summary: Gimp plugin to list image metadata
# There is a line in README stating that license for plugin is "GPL" but file
# COPYING and comments in sources contains in fact something BSD-likeish.
# TODO: ask author for clarification
License: GPL
Group: Graphics

Url: http://registry.gimp.org/plugin?id=4013
Source: metadata.tar.bz2

Requires: gimp >= 2.2

# Automatically added by buildreq on Tue Sep 11 2007
BuildRequires: libgimp-devel

%description
This is a plug-in that lets you interact with Gimp image attachments (often
known as "parasites"). You can list them, view the contents of any that
contain text, create new ones, delete or edit existing ones, load one from a
file, or write one to a file. You can also attach a color profile to an image
(which will be saved by the .tiff format) if you have the .icc file.

%prep
%setup -n metadata

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
# Help and i18n files not packaged 'cause they just stubs now...
%_libdir/gimp/%gimpver/plug-ins/*

%changelog
* Wed Sep 12 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- Initial build.
