Name: gimp-plugin-dbp
Version: 1.1.9
Release: alt1.1

Summary: DBP (David's Batch Processor) Gimp plugin
License: %gpl2plus
Group: Graphics

Url: http://members.ozemail.com.au/~hodsond/dbp.html
Packager: Yury Yurevich <anarresti@altlinux.org>

Source: dbp-%version.tar

BuildPreReq: gcc-c++ >= 4.0
BuildRequires(pre): rpm-build-licenses libgimp-devel

%description
DBP (David's Batch Processor) is a simple batch processing
plugin for the Gimp - it allows the user to automatically
perform operations (such as resize) on a collection of image
files. Its main advantage is that the user does not have
to learn a scripting language. Like the Gimp itself,
DBP relies on a graphical interface. The user creates
a list of images, and sets up the processing required
for each image. The results of the current settings can be
displayed. Once the required sequence of operations has been
set up, DBP performs the same processing on each image in turn.
The images can be colour corrected, resized, cropped,
and sharpened, then renamed and saved to a different file
in a specified image format. All the steps (except loading
and saving the image!) are optional; so the simplest
use of DBP is just to convert a number of image files
from one format to another.

%define _gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins/

%prep
%setup -n dbp-%version

%build
%make_build

%install
install -D dbp %buildroot/%_gimpplugindir/dbp

%files
%_gimpplugindir/dbp
%doc dbp.html

%changelog
* Mon Apr 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.1.9-alt1.1
- Rebuild by mentor

* Sun Apr 12 2009 Yury Yurevich <anarresti@altlinux.org> 1.1.9-alt1
- initial build
