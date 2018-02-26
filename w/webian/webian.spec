Name: webian
Version: 0.1
Release: alt1

Summary: Webian Shell is a graphical shell for the web
License: GPL 3.0+
Group: Networking/WWW
Url: https://github.com/webianproject/

Packager: Paul Wolneykien <manowar@altlinux.ru>
Source: %name-%version.tar

Requires: chromeless

BuildArch: noarch

%description
Webian Shell is a graphical shell for the web, a full screen web browser
for devices that don't need a desktop.

It's an implementation of a design concept called "A Graphical Shell for
the Web" by Ben Francis.

The code is designed to be run using Mozilla Chromeless.

%define webiandir %_datadir/webian

%prep
%setup

%install
# Install the files.
mkdir -m0755 -p %buildroot%webiandir
cp -R --preserve=mode,timestamps *.html *.css *.js *.json *.png %buildroot%webiandir/
install -D -m0755 webian-shell %buildroot%_bindir/webian-shell

# Configure the wrapper.
sed -i -e 's|/usr/local/share/webian|%webiandir|g' %buildroot%_bindir/webian-shell

%files
%webiandir
%_bindir/webian-shell
%doc AUTHORS README

%changelog
* Thu Jul 14 2011 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt1
- Add a startup wrapper.
- Updated AUTHORS file following recent contributions (thx Ben Francis).
- A bit of css tweaking to fix the clocking alignment
  bug. https://github.com/webianproject/shell/issues/91
  (thx Michael Lee).
- Close tab keyboard shortcut
  (https://www.pivotaltracker.com/story/show/9082653)  based on
  carli2's code submissions (thx Ben Francis).
- Started on Keyboard shortcuts story
  (https://www.pivotaltracker.com/story/show/9082653)
  based on carli2's code
  (https://github.com/carli2/webshell/commit/3a4d29e04a20ddbb8b2d58d3aaf589be8b624829)
  (thx Ben Francis).
- added iFrame default background-color (thx Maarten Jacobs).
- preventing default dragging of homescreen background (thx Maarten
  Jacobs).
- added default background-color to iFrame if transparent (thx Maarten
  Jacobs).
- moved faviconUpdate call to iframe load event to fix favicon
  load issue (thx Maarten Jacobs).
- Updated AUTHORS to include all contributors so far (thx Ben Francis).
- Making the full screen web browser full screen again! (thx Ben
  Francis).
- refactored as much as possible (thx Maarten Jacobs).
- Moved the tab listeners for adding of rearranging of tabs and
  added rearranging of tabs! (thx Maarten Jacobs).
- Called focus when registering window event listeners to give
  autofocus feature (thx Maarten Jacobs).
- Called faviconUpdate when going back and forward (thx Maarten Jacobs).
- wrapped home input tag in div to prevent stretching (thx Maarten
  Jacobs).
- Changed tab type to image tag and gave it a style accordingly (thx
  Maarten Jacobs).
- changed new tab button to an actual image and gave it according css
  (thx Maarten Jacobs).
- Adding AUTHORS file (thx Ben Francis).
- Fix youtube reset issue when switching tabs (thx davidmurdoch).
- Applying changes for 0.1 release from subversion repo (thx Ben
  Francis).
