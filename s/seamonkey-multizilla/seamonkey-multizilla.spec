Name: seamonkey-multizilla
Version: 1.8.3.0
Release: alt2
License: MPL
Group: Networking/WWW
URL: http://multizilla.mozdev.org
Source0: http://multizilla.mozdev.org/download.php/http://downloads.mozdev.org/multizilla/multiviews-v1830.xpi

Packager: Damir Shayhutdinov <damir@altlinux.ru>

BuildRequires(pre): rpm-build-seamonkey 
BuildRequires: unzip

Requires: seamonkey

Summary: Tabbed UI extension for Seamonkey
%description
MultiZilla was the first browser extension to introduce the tabbed UI for Seamonkey/Mozilla.

Current Seamonkey/Mozilla builds make use of this idea but it is only partly integrated by the Seamonkey/Mozilla team, so MultiZilla still has lots of extra features that cannot be found in today's Seamonkey/Mozilla builds (although Firefox adds even more MultiZilla features like middle-click on bookmarks and some of the tab group features).

%prep
%setup -c

%install
mkdir -p %buildroot/%seamonkey_chromedir  %buildroot/%seamonkey_defaultsdir/{pref,profile}
cp multiviews.jar %buildroot/%seamonkey_chromedir/
cp all-mz.js %buildroot/%seamonkey_defaultsdir/pref/
mkdir -p %buildroot/%seamonkey_componentsdir/
cp mzUpdateNotifier.js mzContentBlocker.js mzWebFeeds.{js,xpt} %buildroot/%seamonkey_componentsdir/
cp multizilla.rdf useragents.rdf mzWebFeeds.rdf default-filters.rdf \
	%buildroot/%seamonkey_defaultsdir/profile/
cat > installed-chrome.txt <<EOF
content,install,url,jar:resource:/chrome/multiviews.jar!/content/multiviews/
locale,install,url,jar:resource:/chrome/multiviews.jar!/locale/en-US/multiviews/
skin,install,url,jar:resource:/chrome/multiviews.jar!/skin/modern/multiviews/
skin,install,url,jar:resource:/chrome/multiviews.jar!/skin/classic/multiviews/
EOF
cp installed-chrome.txt %buildroot/%seamonkey_chromedir/installed-chrome-multiviews.txt

%post 
%seamonkey_extension_postin

%postun 
%seamonkey_extension_postun

%files
%seamonkey_chromedir/*
%seamonkey_componentsdir/*
%seamonkey_defaultsdir/pref/*
%seamonkey_defaultsdir/profile/*

%changelog
* Tue Nov 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.8.3.0-alt2
- Built with rpm-build-seamonkey 

* Sat Nov 18 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.8.3.0-alt1
- Initial build for ALT Linux.

