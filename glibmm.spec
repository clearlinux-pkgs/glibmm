#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : glibmm
Version  : 2.84.0
Release  : 36
URL      : https://download.gnome.org/sources/glibmm/2.84/glibmm-2.84.0.tar.xz
Source0  : https://download.gnome.org/sources/glibmm/2.84/glibmm-2.84.0.tar.xz
Summary  : C++ wrapper for GLib
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: glibmm-lib = %{version}-%{release}
Requires: glibmm-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : libsigc++-dev
BuildRequires : pkgconfig(mm-common-libstdc++)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains files not tracked by a source code control program,
The files can have one of two origins.

%package dev
Summary: dev components for the glibmm package.
Group: Development
Requires: glibmm-lib = %{version}-%{release}
Provides: glibmm-devel = %{version}-%{release}
Requires: glibmm = %{version}-%{release}

%description dev
dev components for the glibmm package.


%package lib
Summary: lib components for the glibmm package.
Group: Libraries
Requires: glibmm-license = %{version}-%{release}

%description lib
lib components for the glibmm package.


%package license
Summary: license components for the glibmm package.
Group: Default

%description license
license components for the glibmm package.


%prep
%setup -q -n glibmm-2.84.0
cd %{_builddir}/glibmm-2.84.0
pushd ..
cp -a glibmm-2.84.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742407032
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/glibmm
cp %{_builddir}/glibmm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/glibmm/10b7ed0f3f2cfe72fe0c64c167033cbbf8e62d93 || :
cp %{_builddir}/glibmm-%{version}/COPYING.tools %{buildroot}/usr/share/package-licenses/glibmm/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/glibmm-2.68/proc/generate_wrap_init.pl
/usr/lib64/glibmm-2.68/proc/gmmproc
/usr/lib64/glibmm-2.68/proc/m4/base.m4
/usr/lib64/glibmm-2.68/proc/m4/class_boxedtype.m4
/usr/lib64/glibmm-2.68/proc/m4/class_boxedtype_static.m4
/usr/lib64/glibmm-2.68/proc/m4/class_generic.m4
/usr/lib64/glibmm-2.68/proc/m4/class_gobject.m4
/usr/lib64/glibmm-2.68/proc/m4/class_interface.m4
/usr/lib64/glibmm-2.68/proc/m4/class_opaque_copyable.m4
/usr/lib64/glibmm-2.68/proc/m4/class_opaque_refcounted.m4
/usr/lib64/glibmm-2.68/proc/m4/class_shared.m4
/usr/lib64/glibmm-2.68/proc/m4/compare.m4
/usr/lib64/glibmm-2.68/proc/m4/convert.m4
/usr/lib64/glibmm-2.68/proc/m4/convert_base.m4
/usr/lib64/glibmm-2.68/proc/m4/convert_gio.m4
/usr/lib64/glibmm-2.68/proc/m4/convert_glib.m4
/usr/lib64/glibmm-2.68/proc/m4/convert_glibmm.m4
/usr/lib64/glibmm-2.68/proc/m4/ctor.m4
/usr/lib64/glibmm-2.68/proc/m4/doc.m4
/usr/lib64/glibmm-2.68/proc/m4/enum.m4
/usr/lib64/glibmm-2.68/proc/m4/gerror.m4
/usr/lib64/glibmm-2.68/proc/m4/initialize.m4
/usr/lib64/glibmm-2.68/proc/m4/initialize_base.m4
/usr/lib64/glibmm-2.68/proc/m4/initialize_gio.m4
/usr/lib64/glibmm-2.68/proc/m4/initialize_glib.m4
/usr/lib64/glibmm-2.68/proc/m4/initialize_glibmm.m4
/usr/lib64/glibmm-2.68/proc/m4/member.m4
/usr/lib64/glibmm-2.68/proc/m4/method.m4
/usr/lib64/glibmm-2.68/proc/m4/property.m4
/usr/lib64/glibmm-2.68/proc/m4/signal.m4
/usr/lib64/glibmm-2.68/proc/m4/vfunc.m4
/usr/lib64/glibmm-2.68/proc/pm/DocsParser.pm
/usr/lib64/glibmm-2.68/proc/pm/Enum.pm
/usr/lib64/glibmm-2.68/proc/pm/Function.pm
/usr/lib64/glibmm-2.68/proc/pm/FunctionBase.pm
/usr/lib64/glibmm-2.68/proc/pm/GtkDefs.pm
/usr/lib64/glibmm-2.68/proc/pm/Object.pm
/usr/lib64/glibmm-2.68/proc/pm/Output.pm
/usr/lib64/glibmm-2.68/proc/pm/Property.pm
/usr/lib64/glibmm-2.68/proc/pm/Util.pm
/usr/lib64/glibmm-2.68/proc/pm/WrapParser.pm

%files dev
%defattr(-,root,root,-)
/usr/include/giomm-2.68/giomm.h
/usr/include/giomm-2.68/giomm/action.h
/usr/include/giomm-2.68/giomm/actiongroup.h
/usr/include/giomm-2.68/giomm/actionmap.h
/usr/include/giomm-2.68/giomm/appinfo.h
/usr/include/giomm-2.68/giomm/appinfomonitor.h
/usr/include/giomm-2.68/giomm/applaunchcontext.h
/usr/include/giomm-2.68/giomm/application.h
/usr/include/giomm-2.68/giomm/applicationcommandline.h
/usr/include/giomm-2.68/giomm/asyncinitable.h
/usr/include/giomm-2.68/giomm/asyncresult.h
/usr/include/giomm-2.68/giomm/bufferedinputstream.h
/usr/include/giomm-2.68/giomm/bufferedoutputstream.h
/usr/include/giomm-2.68/giomm/bytesicon.h
/usr/include/giomm-2.68/giomm/cancellable.h
/usr/include/giomm-2.68/giomm/charsetconverter.h
/usr/include/giomm-2.68/giomm/contenttype.h
/usr/include/giomm-2.68/giomm/converter.h
/usr/include/giomm-2.68/giomm/converterinputstream.h
/usr/include/giomm-2.68/giomm/converteroutputstream.h
/usr/include/giomm-2.68/giomm/credentials.h
/usr/include/giomm-2.68/giomm/datainputstream.h
/usr/include/giomm-2.68/giomm/dataoutputstream.h
/usr/include/giomm-2.68/giomm/dbusactiongroup.h
/usr/include/giomm-2.68/giomm/dbusaddress.h
/usr/include/giomm-2.68/giomm/dbusauthobserver.h
/usr/include/giomm-2.68/giomm/dbusconnection.h
/usr/include/giomm-2.68/giomm/dbuserror.h
/usr/include/giomm-2.68/giomm/dbuserrorutils.h
/usr/include/giomm-2.68/giomm/dbusinterface.h
/usr/include/giomm-2.68/giomm/dbusinterfaceskeleton.h
/usr/include/giomm-2.68/giomm/dbusinterfacevtable.h
/usr/include/giomm-2.68/giomm/dbusintrospection.h
/usr/include/giomm-2.68/giomm/dbusmenumodel.h
/usr/include/giomm-2.68/giomm/dbusmessage.h
/usr/include/giomm-2.68/giomm/dbusmethodinvocation.h
/usr/include/giomm-2.68/giomm/dbusobject.h
/usr/include/giomm-2.68/giomm/dbusobjectmanager.h
/usr/include/giomm-2.68/giomm/dbusobjectmanagerclient.h
/usr/include/giomm-2.68/giomm/dbusobjectmanagerserver.h
/usr/include/giomm-2.68/giomm/dbusobjectproxy.h
/usr/include/giomm-2.68/giomm/dbusobjectskeleton.h
/usr/include/giomm-2.68/giomm/dbusownname.h
/usr/include/giomm-2.68/giomm/dbusproxy.h
/usr/include/giomm-2.68/giomm/dbusserver.h
/usr/include/giomm-2.68/giomm/dbussubtreevtable.h
/usr/include/giomm-2.68/giomm/dbusutils.h
/usr/include/giomm-2.68/giomm/dbuswatchname.h
/usr/include/giomm-2.68/giomm/desktopappinfo.h
/usr/include/giomm-2.68/giomm/drive.h
/usr/include/giomm-2.68/giomm/emblem.h
/usr/include/giomm-2.68/giomm/emblemedicon.h
/usr/include/giomm-2.68/giomm/enums.h
/usr/include/giomm-2.68/giomm/error.h
/usr/include/giomm-2.68/giomm/file.h
/usr/include/giomm-2.68/giomm/fileattributeinfo.h
/usr/include/giomm-2.68/giomm/fileattributeinfolist.h
/usr/include/giomm-2.68/giomm/filedescriptorbased.h
/usr/include/giomm-2.68/giomm/fileenumerator.h
/usr/include/giomm-2.68/giomm/fileicon.h
/usr/include/giomm-2.68/giomm/fileinfo.h
/usr/include/giomm-2.68/giomm/fileinputstream.h
/usr/include/giomm-2.68/giomm/fileiostream.h
/usr/include/giomm-2.68/giomm/filemonitor.h
/usr/include/giomm-2.68/giomm/filenamecompleter.h
/usr/include/giomm-2.68/giomm/fileoutputstream.h
/usr/include/giomm-2.68/giomm/filterinputstream.h
/usr/include/giomm-2.68/giomm/filteroutputstream.h
/usr/include/giomm-2.68/giomm/icon.h
/usr/include/giomm-2.68/giomm/inetaddress.h
/usr/include/giomm-2.68/giomm/inetsocketaddress.h
/usr/include/giomm-2.68/giomm/init.h
/usr/include/giomm-2.68/giomm/initable.h
/usr/include/giomm-2.68/giomm/inputstream.h
/usr/include/giomm-2.68/giomm/iostream.h
/usr/include/giomm-2.68/giomm/listmodel.h
/usr/include/giomm-2.68/giomm/liststore.h
/usr/include/giomm-2.68/giomm/loadableicon.h
/usr/include/giomm-2.68/giomm/memoryinputstream.h
/usr/include/giomm-2.68/giomm/memoryoutputstream.h
/usr/include/giomm-2.68/giomm/menu.h
/usr/include/giomm-2.68/giomm/menuattributeiter.h
/usr/include/giomm-2.68/giomm/menuitem.h
/usr/include/giomm-2.68/giomm/menulinkiter.h
/usr/include/giomm-2.68/giomm/menumodel.h
/usr/include/giomm-2.68/giomm/mount.h
/usr/include/giomm-2.68/giomm/mountoperation.h
/usr/include/giomm-2.68/giomm/networkaddress.h
/usr/include/giomm-2.68/giomm/networkmonitor.h
/usr/include/giomm-2.68/giomm/networkservice.h
/usr/include/giomm-2.68/giomm/notification.h
/usr/include/giomm-2.68/giomm/outputstream.h
/usr/include/giomm-2.68/giomm/permission.h
/usr/include/giomm-2.68/giomm/pollableinputstream.h
/usr/include/giomm-2.68/giomm/pollableoutputstream.h
/usr/include/giomm-2.68/giomm/private/action_p.h
/usr/include/giomm-2.68/giomm/private/actiongroup_p.h
/usr/include/giomm-2.68/giomm/private/actionmap_p.h
/usr/include/giomm-2.68/giomm/private/appinfo_p.h
/usr/include/giomm-2.68/giomm/private/appinfomonitor_p.h
/usr/include/giomm-2.68/giomm/private/applaunchcontext_p.h
/usr/include/giomm-2.68/giomm/private/application_p.h
/usr/include/giomm-2.68/giomm/private/applicationcommandline_p.h
/usr/include/giomm-2.68/giomm/private/asyncinitable_p.h
/usr/include/giomm-2.68/giomm/private/asyncresult_p.h
/usr/include/giomm-2.68/giomm/private/bufferedinputstream_p.h
/usr/include/giomm-2.68/giomm/private/bufferedoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/bytesicon_p.h
/usr/include/giomm-2.68/giomm/private/cancellable_p.h
/usr/include/giomm-2.68/giomm/private/charsetconverter_p.h
/usr/include/giomm-2.68/giomm/private/converter_p.h
/usr/include/giomm-2.68/giomm/private/converterinputstream_p.h
/usr/include/giomm-2.68/giomm/private/converteroutputstream_p.h
/usr/include/giomm-2.68/giomm/private/credentials_p.h
/usr/include/giomm-2.68/giomm/private/datainputstream_p.h
/usr/include/giomm-2.68/giomm/private/dataoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/dbusactiongroup_p.h
/usr/include/giomm-2.68/giomm/private/dbusaddress_p.h
/usr/include/giomm-2.68/giomm/private/dbusauthobserver_p.h
/usr/include/giomm-2.68/giomm/private/dbusconnection_p.h
/usr/include/giomm-2.68/giomm/private/dbuserror_p.h
/usr/include/giomm-2.68/giomm/private/dbuserrorutils_p.h
/usr/include/giomm-2.68/giomm/private/dbusinterface_p.h
/usr/include/giomm-2.68/giomm/private/dbusinterfaceskeleton_p.h
/usr/include/giomm-2.68/giomm/private/dbusinterfacevtable_p.h
/usr/include/giomm-2.68/giomm/private/dbusintrospection_p.h
/usr/include/giomm-2.68/giomm/private/dbusmenumodel_p.h
/usr/include/giomm-2.68/giomm/private/dbusmessage_p.h
/usr/include/giomm-2.68/giomm/private/dbusmethodinvocation_p.h
/usr/include/giomm-2.68/giomm/private/dbusobject_p.h
/usr/include/giomm-2.68/giomm/private/dbusobjectmanager_p.h
/usr/include/giomm-2.68/giomm/private/dbusobjectmanagerclient_p.h
/usr/include/giomm-2.68/giomm/private/dbusobjectmanagerserver_p.h
/usr/include/giomm-2.68/giomm/private/dbusobjectproxy_p.h
/usr/include/giomm-2.68/giomm/private/dbusobjectskeleton_p.h
/usr/include/giomm-2.68/giomm/private/dbusownname_p.h
/usr/include/giomm-2.68/giomm/private/dbusproxy_p.h
/usr/include/giomm-2.68/giomm/private/dbusserver_p.h
/usr/include/giomm-2.68/giomm/private/dbussubtreevtable_p.h
/usr/include/giomm-2.68/giomm/private/dbusutils_p.h
/usr/include/giomm-2.68/giomm/private/dbuswatchname_p.h
/usr/include/giomm-2.68/giomm/private/desktopappinfo_p.h
/usr/include/giomm-2.68/giomm/private/drive_p.h
/usr/include/giomm-2.68/giomm/private/emblem_p.h
/usr/include/giomm-2.68/giomm/private/emblemedicon_p.h
/usr/include/giomm-2.68/giomm/private/enums_p.h
/usr/include/giomm-2.68/giomm/private/error_p.h
/usr/include/giomm-2.68/giomm/private/file_p.h
/usr/include/giomm-2.68/giomm/private/fileattributeinfo_p.h
/usr/include/giomm-2.68/giomm/private/fileattributeinfolist_p.h
/usr/include/giomm-2.68/giomm/private/filedescriptorbased_p.h
/usr/include/giomm-2.68/giomm/private/fileenumerator_p.h
/usr/include/giomm-2.68/giomm/private/fileicon_p.h
/usr/include/giomm-2.68/giomm/private/fileinfo_p.h
/usr/include/giomm-2.68/giomm/private/fileinputstream_p.h
/usr/include/giomm-2.68/giomm/private/fileiostream_p.h
/usr/include/giomm-2.68/giomm/private/filemonitor_p.h
/usr/include/giomm-2.68/giomm/private/filenamecompleter_p.h
/usr/include/giomm-2.68/giomm/private/fileoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/filterinputstream_p.h
/usr/include/giomm-2.68/giomm/private/filteroutputstream_p.h
/usr/include/giomm-2.68/giomm/private/icon_p.h
/usr/include/giomm-2.68/giomm/private/inetaddress_p.h
/usr/include/giomm-2.68/giomm/private/inetsocketaddress_p.h
/usr/include/giomm-2.68/giomm/private/initable_p.h
/usr/include/giomm-2.68/giomm/private/inputstream_p.h
/usr/include/giomm-2.68/giomm/private/iostream_p.h
/usr/include/giomm-2.68/giomm/private/listmodel_p.h
/usr/include/giomm-2.68/giomm/private/liststore_p.h
/usr/include/giomm-2.68/giomm/private/loadableicon_p.h
/usr/include/giomm-2.68/giomm/private/memoryinputstream_p.h
/usr/include/giomm-2.68/giomm/private/memoryoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/menu_p.h
/usr/include/giomm-2.68/giomm/private/menuattributeiter_p.h
/usr/include/giomm-2.68/giomm/private/menuitem_p.h
/usr/include/giomm-2.68/giomm/private/menulinkiter_p.h
/usr/include/giomm-2.68/giomm/private/menumodel_p.h
/usr/include/giomm-2.68/giomm/private/mount_p.h
/usr/include/giomm-2.68/giomm/private/mountoperation_p.h
/usr/include/giomm-2.68/giomm/private/networkaddress_p.h
/usr/include/giomm-2.68/giomm/private/networkmonitor_p.h
/usr/include/giomm-2.68/giomm/private/networkservice_p.h
/usr/include/giomm-2.68/giomm/private/notification_p.h
/usr/include/giomm-2.68/giomm/private/outputstream_p.h
/usr/include/giomm-2.68/giomm/private/permission_p.h
/usr/include/giomm-2.68/giomm/private/pollableinputstream_p.h
/usr/include/giomm-2.68/giomm/private/pollableoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/propertyaction_p.h
/usr/include/giomm-2.68/giomm/private/proxy_p.h
/usr/include/giomm-2.68/giomm/private/proxyaddress_p.h
/usr/include/giomm-2.68/giomm/private/proxyresolver_p.h
/usr/include/giomm-2.68/giomm/private/remoteactiongroup_p.h
/usr/include/giomm-2.68/giomm/private/resolver_p.h
/usr/include/giomm-2.68/giomm/private/resource_p.h
/usr/include/giomm-2.68/giomm/private/seekable_p.h
/usr/include/giomm-2.68/giomm/private/settings_p.h
/usr/include/giomm-2.68/giomm/private/settingsschema_p.h
/usr/include/giomm-2.68/giomm/private/settingsschemakey_p.h
/usr/include/giomm-2.68/giomm/private/settingsschemasource_p.h
/usr/include/giomm-2.68/giomm/private/simpleaction_p.h
/usr/include/giomm-2.68/giomm/private/simpleactiongroup_p.h
/usr/include/giomm-2.68/giomm/private/simpleiostream_p.h
/usr/include/giomm-2.68/giomm/private/simplepermission_p.h
/usr/include/giomm-2.68/giomm/private/socket_p.h
/usr/include/giomm-2.68/giomm/private/socketaddress_p.h
/usr/include/giomm-2.68/giomm/private/socketaddressenumerator_p.h
/usr/include/giomm-2.68/giomm/private/socketclient_p.h
/usr/include/giomm-2.68/giomm/private/socketconnectable_p.h
/usr/include/giomm-2.68/giomm/private/socketconnection_p.h
/usr/include/giomm-2.68/giomm/private/socketcontrolmessage_p.h
/usr/include/giomm-2.68/giomm/private/socketlistener_p.h
/usr/include/giomm-2.68/giomm/private/socketservice_p.h
/usr/include/giomm-2.68/giomm/private/srvtarget_p.h
/usr/include/giomm-2.68/giomm/private/subprocess_p.h
/usr/include/giomm-2.68/giomm/private/subprocesslauncher_p.h
/usr/include/giomm-2.68/giomm/private/tcpconnection_p.h
/usr/include/giomm-2.68/giomm/private/tcpwrapperconnection_p.h
/usr/include/giomm-2.68/giomm/private/themedicon_p.h
/usr/include/giomm-2.68/giomm/private/threadedsocketservice_p.h
/usr/include/giomm-2.68/giomm/private/tlscertificate_p.h
/usr/include/giomm-2.68/giomm/private/tlsclientconnection_p.h
/usr/include/giomm-2.68/giomm/private/tlsconnection_p.h
/usr/include/giomm-2.68/giomm/private/tlsdatabase_p.h
/usr/include/giomm-2.68/giomm/private/tlsinteraction_p.h
/usr/include/giomm-2.68/giomm/private/tlspassword_p.h
/usr/include/giomm-2.68/giomm/private/tlsserverconnection_p.h
/usr/include/giomm-2.68/giomm/private/unixconnection_p.h
/usr/include/giomm-2.68/giomm/private/unixcredentialsmessage_p.h
/usr/include/giomm-2.68/giomm/private/unixfdlist_p.h
/usr/include/giomm-2.68/giomm/private/unixfdmessage_p.h
/usr/include/giomm-2.68/giomm/private/unixinputstream_p.h
/usr/include/giomm-2.68/giomm/private/unixoutputstream_p.h
/usr/include/giomm-2.68/giomm/private/unixsocketaddress_p.h
/usr/include/giomm-2.68/giomm/private/volume_p.h
/usr/include/giomm-2.68/giomm/private/volumemonitor_p.h
/usr/include/giomm-2.68/giomm/private/zlibcompressor_p.h
/usr/include/giomm-2.68/giomm/private/zlibdecompressor_p.h
/usr/include/giomm-2.68/giomm/propertyaction.h
/usr/include/giomm-2.68/giomm/proxy.h
/usr/include/giomm-2.68/giomm/proxyaddress.h
/usr/include/giomm-2.68/giomm/proxyresolver.h
/usr/include/giomm-2.68/giomm/remoteactiongroup.h
/usr/include/giomm-2.68/giomm/resolver.h
/usr/include/giomm-2.68/giomm/resource.h
/usr/include/giomm-2.68/giomm/seekable.h
/usr/include/giomm-2.68/giomm/settings.h
/usr/include/giomm-2.68/giomm/settingsschema.h
/usr/include/giomm-2.68/giomm/settingsschemakey.h
/usr/include/giomm-2.68/giomm/settingsschemasource.h
/usr/include/giomm-2.68/giomm/simpleaction.h
/usr/include/giomm-2.68/giomm/simpleactiongroup.h
/usr/include/giomm-2.68/giomm/simpleiostream.h
/usr/include/giomm-2.68/giomm/simplepermission.h
/usr/include/giomm-2.68/giomm/slot_async.h
/usr/include/giomm-2.68/giomm/socket.h
/usr/include/giomm-2.68/giomm/socketaddress.h
/usr/include/giomm-2.68/giomm/socketaddressenumerator.h
/usr/include/giomm-2.68/giomm/socketclient.h
/usr/include/giomm-2.68/giomm/socketconnectable.h
/usr/include/giomm-2.68/giomm/socketconnection.h
/usr/include/giomm-2.68/giomm/socketcontrolmessage.h
/usr/include/giomm-2.68/giomm/socketlistener.h
/usr/include/giomm-2.68/giomm/socketservice.h
/usr/include/giomm-2.68/giomm/socketsource.h
/usr/include/giomm-2.68/giomm/srvtarget.h
/usr/include/giomm-2.68/giomm/subprocess.h
/usr/include/giomm-2.68/giomm/subprocesslauncher.h
/usr/include/giomm-2.68/giomm/tcpconnection.h
/usr/include/giomm-2.68/giomm/tcpwrapperconnection.h
/usr/include/giomm-2.68/giomm/themedicon.h
/usr/include/giomm-2.68/giomm/threadedsocketservice.h
/usr/include/giomm-2.68/giomm/tlscertificate.h
/usr/include/giomm-2.68/giomm/tlsclientconnection.h
/usr/include/giomm-2.68/giomm/tlsclientconnectionimpl.h
/usr/include/giomm-2.68/giomm/tlsconnection.h
/usr/include/giomm-2.68/giomm/tlsdatabase.h
/usr/include/giomm-2.68/giomm/tlsinteraction.h
/usr/include/giomm-2.68/giomm/tlspassword.h
/usr/include/giomm-2.68/giomm/tlsserverconnection.h
/usr/include/giomm-2.68/giomm/tlsserverconnectionimpl.h
/usr/include/giomm-2.68/giomm/unixconnection.h
/usr/include/giomm-2.68/giomm/unixcredentialsmessage.h
/usr/include/giomm-2.68/giomm/unixfdlist.h
/usr/include/giomm-2.68/giomm/unixfdmessage.h
/usr/include/giomm-2.68/giomm/unixinputstream.h
/usr/include/giomm-2.68/giomm/unixoutputstream.h
/usr/include/giomm-2.68/giomm/unixsocketaddress.h
/usr/include/giomm-2.68/giomm/volume.h
/usr/include/giomm-2.68/giomm/volumemonitor.h
/usr/include/giomm-2.68/giomm/wrap_init.h
/usr/include/giomm-2.68/giomm/zlibcompressor.h
/usr/include/giomm-2.68/giomm/zlibdecompressor.h
/usr/include/glibmm-2.68/glibmm.h
/usr/include/glibmm-2.68/glibmm/base64.h
/usr/include/glibmm-2.68/glibmm/binding.h
/usr/include/glibmm-2.68/glibmm/bytearray.h
/usr/include/glibmm-2.68/glibmm/bytes.h
/usr/include/glibmm-2.68/glibmm/checksum.h
/usr/include/glibmm-2.68/glibmm/class.h
/usr/include/glibmm-2.68/glibmm/containerhandle_shared.h
/usr/include/glibmm-2.68/glibmm/convert.h
/usr/include/glibmm-2.68/glibmm/date.h
/usr/include/glibmm-2.68/glibmm/datetime.h
/usr/include/glibmm-2.68/glibmm/debug.h
/usr/include/glibmm-2.68/glibmm/dispatcher.h
/usr/include/glibmm-2.68/glibmm/enums.h
/usr/include/glibmm-2.68/glibmm/environ.h
/usr/include/glibmm-2.68/glibmm/error.h
/usr/include/glibmm-2.68/glibmm/exceptionhandler.h
/usr/include/glibmm-2.68/glibmm/extraclassinit.h
/usr/include/glibmm-2.68/glibmm/fileutils.h
/usr/include/glibmm-2.68/glibmm/i18n-lib.h
/usr/include/glibmm-2.68/glibmm/i18n.h
/usr/include/glibmm-2.68/glibmm/init.h
/usr/include/glibmm-2.68/glibmm/interface.h
/usr/include/glibmm-2.68/glibmm/iochannel.h
/usr/include/glibmm-2.68/glibmm/keyfile.h
/usr/include/glibmm-2.68/glibmm/main.h
/usr/include/glibmm-2.68/glibmm/markup.h
/usr/include/glibmm-2.68/glibmm/miscutils.h
/usr/include/glibmm-2.68/glibmm/module.h
/usr/include/glibmm-2.68/glibmm/nodetree.h
/usr/include/glibmm-2.68/glibmm/object.h
/usr/include/glibmm-2.68/glibmm/objectbase.h
/usr/include/glibmm-2.68/glibmm/optioncontext.h
/usr/include/glibmm-2.68/glibmm/optionentry.h
/usr/include/glibmm-2.68/glibmm/optiongroup.h
/usr/include/glibmm-2.68/glibmm/pattern.h
/usr/include/glibmm-2.68/glibmm/priorities.h
/usr/include/glibmm-2.68/glibmm/private/binding_p.h
/usr/include/glibmm-2.68/glibmm/private/bytearray_p.h
/usr/include/glibmm-2.68/glibmm/private/bytes_p.h
/usr/include/glibmm-2.68/glibmm/private/checksum_p.h
/usr/include/glibmm-2.68/glibmm/private/convert_p.h
/usr/include/glibmm-2.68/glibmm/private/date_p.h
/usr/include/glibmm-2.68/glibmm/private/datetime_p.h
/usr/include/glibmm-2.68/glibmm/private/enums_p.h
/usr/include/glibmm-2.68/glibmm/private/fileutils_p.h
/usr/include/glibmm-2.68/glibmm/private/interface_p.h
/usr/include/glibmm-2.68/glibmm/private/iochannel_p.h
/usr/include/glibmm-2.68/glibmm/private/keyfile_p.h
/usr/include/glibmm-2.68/glibmm/private/markup_p.h
/usr/include/glibmm-2.68/glibmm/private/miscutils_p.h
/usr/include/glibmm-2.68/glibmm/private/module_p.h
/usr/include/glibmm-2.68/glibmm/private/nodetree_p.h
/usr/include/glibmm-2.68/glibmm/private/object_p.h
/usr/include/glibmm-2.68/glibmm/private/optioncontext_p.h
/usr/include/glibmm-2.68/glibmm/private/optionentry_p.h
/usr/include/glibmm-2.68/glibmm/private/optiongroup_p.h
/usr/include/glibmm-2.68/glibmm/private/regex_p.h
/usr/include/glibmm-2.68/glibmm/private/shell_p.h
/usr/include/glibmm-2.68/glibmm/private/spawn_p.h
/usr/include/glibmm-2.68/glibmm/private/timezone_p.h
/usr/include/glibmm-2.68/glibmm/private/unicode_p.h
/usr/include/glibmm-2.68/glibmm/private/uriutils_p.h
/usr/include/glibmm-2.68/glibmm/private/variant_p.h
/usr/include/glibmm-2.68/glibmm/private/variantdict_p.h
/usr/include/glibmm-2.68/glibmm/private/variantiter_p.h
/usr/include/glibmm-2.68/glibmm/private/varianttype_p.h
/usr/include/glibmm-2.68/glibmm/property.h
/usr/include/glibmm-2.68/glibmm/propertyproxy.h
/usr/include/glibmm-2.68/glibmm/propertyproxy_base.h
/usr/include/glibmm-2.68/glibmm/quark.h
/usr/include/glibmm-2.68/glibmm/random.h
/usr/include/glibmm-2.68/glibmm/refptr.h
/usr/include/glibmm-2.68/glibmm/regex.h
/usr/include/glibmm-2.68/glibmm/shell.h
/usr/include/glibmm-2.68/glibmm/signalproxy.h
/usr/include/glibmm-2.68/glibmm/signalproxy_connectionnode.h
/usr/include/glibmm-2.68/glibmm/spawn.h
/usr/include/glibmm-2.68/glibmm/stringutils.h
/usr/include/glibmm-2.68/glibmm/timer.h
/usr/include/glibmm-2.68/glibmm/timezone.h
/usr/include/glibmm-2.68/glibmm/unicode.h
/usr/include/glibmm-2.68/glibmm/uriutils.h
/usr/include/glibmm-2.68/glibmm/ustring.h
/usr/include/glibmm-2.68/glibmm/ustring_hash.h
/usr/include/glibmm-2.68/glibmm/utility.h
/usr/include/glibmm-2.68/glibmm/value.h
/usr/include/glibmm-2.68/glibmm/value_basictypes.h
/usr/include/glibmm-2.68/glibmm/value_custom.h
/usr/include/glibmm-2.68/glibmm/variant.h
/usr/include/glibmm-2.68/glibmm/variant_basictypes.h
/usr/include/glibmm-2.68/glibmm/variantdbusstring.h
/usr/include/glibmm-2.68/glibmm/variantdict.h
/usr/include/glibmm-2.68/glibmm/variantiter.h
/usr/include/glibmm-2.68/glibmm/varianttype.h
/usr/include/glibmm-2.68/glibmm/vectorutils.h
/usr/include/glibmm-2.68/glibmm/version.h
/usr/include/glibmm-2.68/glibmm/wrap.h
/usr/include/glibmm-2.68/glibmm/wrap_init.h
/usr/include/glibmm-2.68/glibmm_generate_extra_defs/generate_extra_defs.h
/usr/lib64/giomm-2.68/include/giommconfig.h
/usr/lib64/glibmm-2.68/include/glibmmconfig.h
/usr/lib64/libgiomm-2.68.so
/usr/lib64/libglibmm-2.68.so
/usr/lib64/libglibmm_generate_extra_defs-2.68.so
/usr/lib64/pkgconfig/giomm-2.68.pc
/usr/lib64/pkgconfig/glibmm-2.68.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgiomm-2.68.so.1.3.0
/V3/usr/lib64/libglibmm-2.68.so.1.3.0
/V3/usr/lib64/libglibmm_generate_extra_defs-2.68.so.1.3.0
/usr/lib64/libgiomm-2.68.so.1
/usr/lib64/libgiomm-2.68.so.1.3.0
/usr/lib64/libglibmm-2.68.so.1
/usr/lib64/libglibmm-2.68.so.1.3.0
/usr/lib64/libglibmm_generate_extra_defs-2.68.so.1
/usr/lib64/libglibmm_generate_extra_defs-2.68.so.1.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glibmm/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/glibmm/10b7ed0f3f2cfe72fe0c64c167033cbbf8e62d93
