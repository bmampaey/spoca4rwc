#!/usr/bin/env/python

class _HeliographicCoordinate_Carrington:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.Latitude = Latitude
        self.Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if value is None:
            raise ValueError("Latitude cannot be None")
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if value is None:
            raise ValueError("Longitude cannot be None")
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.Latitude is not None:
            d['Latitude'] = self.Latitude.as_dict() if hasattr(self.Latitude, 'as_dict') else self.Latitude
        if self.Longitude is not None:
            d['Longitude'] = self.Longitude.as_dict() if hasattr(self.Longitude, 'as_dict') else self.Longitude
        return d

class FT__HeliographicCoordinate_Carrington:

    _event_type_enum = ['_HeliographicCoordinate_Carrington', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate_Carrington, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate_Carrington'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, _HeliographicCoordinate_Carrington):
            raise TypeError("data must be _HeliographicCoordinate_Carrington")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class _HeliographicCoordinate_Stonyhurst:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.Latitude = Latitude
        self.Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if value is None:
            raise ValueError("Latitude cannot be None")
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if value is None:
            raise ValueError("Longitude cannot be None")
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.Latitude is not None:
            d['Latitude'] = self.Latitude.as_dict() if hasattr(self.Latitude, 'as_dict') else self.Latitude
        if self.Longitude is not None:
            d['Longitude'] = self.Longitude.as_dict() if hasattr(self.Longitude, 'as_dict') else self.Longitude
        return d

class FT__HeliographicCoordinate_Stonyhurst:

    _event_type_enum = ['_HeliographicCoordinate_Stonyhurst', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate_Stonyhurst'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, _HeliographicCoordinate_Stonyhurst):
            raise TypeError("data must be _HeliographicCoordinate_Stonyhurst")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class SPOCA_CoronalHoleDetectionStatistics:

    _types_map = {
        'ThirdQuartile': {'type': float, 'subtype': None},
        'Skewness': {'type': float, 'subtype': None},
        'Min': {'type': float, 'subtype': None},
        'ImageChannel': {'type': str, 'subtype': None},
        'Max': {'type': float, 'subtype': None},
        'FirstQuartile': {'type': float, 'subtype': None},
        'Median': {'type': float, 'subtype': None},
        'Detection': {'type': list, 'subtype': None},
        'PixelsNumber': {'type': float, 'subtype': None},
        'Var': {'type': float, 'subtype': None},
        'Kurtosis': {'type': float, 'subtype': None},
        'Mean': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , ThirdQuartile=None
            , Skewness=None
            , Min=None
            , ImageChannel=None
            , Max=None
            , FirstQuartile=None
            , Median=None
            , Detection=None
            , PixelsNumber=None
            , Var=None
            , Kurtosis=None
            , Mean=None
            ):
        self.ThirdQuartile = ThirdQuartile
        self.Skewness = Skewness
        self.Min = Min
        self.ImageChannel = ImageChannel
        self.Max = Max
        self.FirstQuartile = FirstQuartile
        self.Median = Median
        self.Detection = Detection
        self.PixelsNumber = PixelsNumber
        self.Var = Var
        self.Kurtosis = Kurtosis
        self.Mean = Mean
    
    def _get_ThirdQuartile(self):
        return self.__ThirdQuartile
    def _set_ThirdQuartile(self, value):
        if value is None:
            raise ValueError("ThirdQuartile cannot be None")
        if not isinstance(value, float):
            raise TypeError("ThirdQuartile must be float")
        self.__ThirdQuartile = value
    ThirdQuartile = property(_get_ThirdQuartile, _set_ThirdQuartile)
    
    def _get_Skewness(self):
        return self.__Skewness
    def _set_Skewness(self, value):
        if value is None:
            raise ValueError("Skewness cannot be None")
        if not isinstance(value, float):
            raise TypeError("Skewness must be float")
        self.__Skewness = value
    Skewness = property(_get_Skewness, _set_Skewness)
    
    def _get_Min(self):
        return self.__Min
    def _set_Min(self, value):
        if value is None:
            raise ValueError("Min cannot be None")
        if not isinstance(value, float):
            raise TypeError("Min must be float")
        self.__Min = value
    Min = property(_get_Min, _set_Min)
    
    def _get_ImageChannel(self):
        return self.__ImageChannel
    def _set_ImageChannel(self, value):
        if value is None:
            raise ValueError("ImageChannel cannot be None")
        if not isinstance(value, str):
            raise TypeError("ImageChannel must be str")
        self.__ImageChannel = value
    ImageChannel = property(_get_ImageChannel, _set_ImageChannel)
    
    def _get_Max(self):
        return self.__Max
    def _set_Max(self, value):
        if value is None:
            raise ValueError("Max cannot be None")
        if not isinstance(value, float):
            raise TypeError("Max must be float")
        self.__Max = value
    Max = property(_get_Max, _set_Max)
    
    def _get_FirstQuartile(self):
        return self.__FirstQuartile
    def _set_FirstQuartile(self, value):
        if value is None:
            raise ValueError("FirstQuartile cannot be None")
        if not isinstance(value, float):
            raise TypeError("FirstQuartile must be float")
        self.__FirstQuartile = value
    FirstQuartile = property(_get_FirstQuartile, _set_FirstQuartile)
    
    def _get_Median(self):
        return self.__Median
    def _set_Median(self, value):
        if value is None:
            raise ValueError("Median cannot be None")
        if not isinstance(value, float):
            raise TypeError("Median must be float")
        self.__Median = value
    Median = property(_get_Median, _set_Median)
    
    def _get_Detection(self):
        return self.__Detection
    def _set_Detection(self, value):
        if value is None:
            raise ValueError("Detection cannot be None")
        if not isinstance(value, list):
            raise TypeError("Detection must be list")
        self.__Detection = value
    Detection = property(_get_Detection, _set_Detection)
    
    def _get_PixelsNumber(self):
        return self.__PixelsNumber
    def _set_PixelsNumber(self, value):
        if value is None:
            raise ValueError("PixelsNumber cannot be None")
        if not isinstance(value, float):
            raise TypeError("PixelsNumber must be float")
        self.__PixelsNumber = value
    PixelsNumber = property(_get_PixelsNumber, _set_PixelsNumber)
    
    def _get_Var(self):
        return self.__Var
    def _set_Var(self, value):
        if value is None:
            raise ValueError("Var cannot be None")
        if not isinstance(value, float):
            raise TypeError("Var must be float")
        self.__Var = value
    Var = property(_get_Var, _set_Var)
    
    def _get_Kurtosis(self):
        return self.__Kurtosis
    def _set_Kurtosis(self, value):
        if value is None:
            raise ValueError("Kurtosis cannot be None")
        if not isinstance(value, float):
            raise TypeError("Kurtosis must be float")
        self.__Kurtosis = value
    Kurtosis = property(_get_Kurtosis, _set_Kurtosis)
    
    def _get_Mean(self):
        return self.__Mean
    def _set_Mean(self, value):
        if value is None:
            raise ValueError("Mean cannot be None")
        if not isinstance(value, float):
            raise TypeError("Mean must be float")
        self.__Mean = value
    Mean = property(_get_Mean, _set_Mean)
    
    def as_dict(self):
        d = dict()
        if self.ThirdQuartile is not None:
            d['ThirdQuartile'] = self.ThirdQuartile.as_dict() if hasattr(self.ThirdQuartile, 'as_dict') else self.ThirdQuartile
        if self.Skewness is not None:
            d['Skewness'] = self.Skewness.as_dict() if hasattr(self.Skewness, 'as_dict') else self.Skewness
        if self.Min is not None:
            d['Min'] = self.Min.as_dict() if hasattr(self.Min, 'as_dict') else self.Min
        if self.ImageChannel is not None:
            d['ImageChannel'] = self.ImageChannel.as_dict() if hasattr(self.ImageChannel, 'as_dict') else self.ImageChannel
        if self.Max is not None:
            d['Max'] = self.Max.as_dict() if hasattr(self.Max, 'as_dict') else self.Max
        if self.FirstQuartile is not None:
            d['FirstQuartile'] = self.FirstQuartile.as_dict() if hasattr(self.FirstQuartile, 'as_dict') else self.FirstQuartile
        if self.Median is not None:
            d['Median'] = self.Median.as_dict() if hasattr(self.Median, 'as_dict') else self.Median
        if self.Detection is not None:
            d['Detection'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Detection]
        if self.PixelsNumber is not None:
            d['PixelsNumber'] = self.PixelsNumber.as_dict() if hasattr(self.PixelsNumber, 'as_dict') else self.PixelsNumber
        if self.Var is not None:
            d['Var'] = self.Var.as_dict() if hasattr(self.Var, 'as_dict') else self.Var
        if self.Kurtosis is not None:
            d['Kurtosis'] = self.Kurtosis.as_dict() if hasattr(self.Kurtosis, 'as_dict') else self.Kurtosis
        if self.Mean is not None:
            d['Mean'] = self.Mean.as_dict() if hasattr(self.Mean, 'as_dict') else self.Mean
        return d

class FT_SPOCA_CoronalHoleDetectionStatistics:

    _event_type_enum = ['SPOCA_CoronalHoleDetectionStatistics', ]
    _types_map = {
        'data': {'type': SPOCA_CoronalHoleDetectionStatistics, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='SPOCA_CoronalHoleDetectionStatistics'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, SPOCA_CoronalHoleDetectionStatistics):
            raise TypeError("data must be SPOCA_CoronalHoleDetectionStatistics")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class _HeliographicCoordinate:

    _types_map = {
        'Carrington': {'type': FT__HeliographicCoordinate_Carrington, 'subtype': None},
        'Stonyhurst': {'type': FT__HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'Time': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'Time': 'date-time',
    }

    def __init__(self
            , Carrington=None
            , Stonyhurst=None
            , Time=None
            ):
        self.Carrington = Carrington
        self.Stonyhurst = Stonyhurst
        self.Time = Time
    
    def _get_Carrington(self):
        return self.__Carrington
    def _set_Carrington(self, value):
        if value is None:
            raise ValueError("Carrington cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Carrington):
            raise TypeError("Carrington must be FT__HeliographicCoordinate_Carrington")
        self.__Carrington = value
    Carrington = property(_get_Carrington, _set_Carrington)
    
    def _get_Stonyhurst(self):
        return self.__Stonyhurst
    def _set_Stonyhurst(self, value):
        if value is None:
            raise ValueError("Stonyhurst cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Stonyhurst):
            raise TypeError("Stonyhurst must be FT__HeliographicCoordinate_Stonyhurst")
        self.__Stonyhurst = value
    Stonyhurst = property(_get_Stonyhurst, _set_Stonyhurst)
    
    def _get_Time(self):
        return self.__Time
    def _set_Time(self, value):
        if value is None:
            raise ValueError("Time cannot be None")
        if not isinstance(value, str):
            raise TypeError("Time must be str")
        self.__Time = value
    Time = property(_get_Time, _set_Time)
    
    def as_dict(self):
        d = dict()
        if self.Carrington is not None:
            d['Carrington'] = self.Carrington.as_dict() if hasattr(self.Carrington, 'as_dict') else self.Carrington
        if self.Stonyhurst is not None:
            d['Stonyhurst'] = self.Stonyhurst.as_dict() if hasattr(self.Stonyhurst, 'as_dict') else self.Stonyhurst
        if self.Time is not None:
            d['Time'] = self.Time.as_dict() if hasattr(self.Time, 'as_dict') else self.Time
        return d

class FT__HeliographicCoordinate:

    _event_type_enum = ['_HeliographicCoordinate', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, _HeliographicCoordinate):
            raise TypeError("data must be _HeliographicCoordinate")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class _SolarSurface_BoundingBox:

    _types_map = {
        'StonyhurstNE': {'type': FT__HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'CarringtonNE': {'type': FT__HeliographicCoordinate_Carrington, 'subtype': None},
        'CarringtonSW': {'type': FT__HeliographicCoordinate_Carrington, 'subtype': None},
        'StonyhurstSW': {'type': FT__HeliographicCoordinate_Stonyhurst, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , StonyhurstNE=None
            , CarringtonNE=None
            , CarringtonSW=None
            , StonyhurstSW=None
            ):
        self.StonyhurstNE = StonyhurstNE
        self.CarringtonNE = CarringtonNE
        self.CarringtonSW = CarringtonSW
        self.StonyhurstSW = StonyhurstSW
    
    def _get_StonyhurstNE(self):
        return self.__StonyhurstNE
    def _set_StonyhurstNE(self, value):
        if value is None:
            raise ValueError("StonyhurstNE cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Stonyhurst):
            raise TypeError("StonyhurstNE must be FT__HeliographicCoordinate_Stonyhurst")
        self.__StonyhurstNE = value
    StonyhurstNE = property(_get_StonyhurstNE, _set_StonyhurstNE)
    
    def _get_CarringtonNE(self):
        return self.__CarringtonNE
    def _set_CarringtonNE(self, value):
        if value is None:
            raise ValueError("CarringtonNE cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Carrington):
            raise TypeError("CarringtonNE must be FT__HeliographicCoordinate_Carrington")
        self.__CarringtonNE = value
    CarringtonNE = property(_get_CarringtonNE, _set_CarringtonNE)
    
    def _get_CarringtonSW(self):
        return self.__CarringtonSW
    def _set_CarringtonSW(self, value):
        if value is None:
            raise ValueError("CarringtonSW cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Carrington):
            raise TypeError("CarringtonSW must be FT__HeliographicCoordinate_Carrington")
        self.__CarringtonSW = value
    CarringtonSW = property(_get_CarringtonSW, _set_CarringtonSW)
    
    def _get_StonyhurstSW(self):
        return self.__StonyhurstSW
    def _set_StonyhurstSW(self, value):
        if value is None:
            raise ValueError("StonyhurstSW cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate_Stonyhurst):
            raise TypeError("StonyhurstSW must be FT__HeliographicCoordinate_Stonyhurst")
        self.__StonyhurstSW = value
    StonyhurstSW = property(_get_StonyhurstSW, _set_StonyhurstSW)
    
    def as_dict(self):
        d = dict()
        if self.StonyhurstNE is not None:
            d['StonyhurstNE'] = self.StonyhurstNE.as_dict() if hasattr(self.StonyhurstNE, 'as_dict') else self.StonyhurstNE
        if self.CarringtonNE is not None:
            d['CarringtonNE'] = self.CarringtonNE.as_dict() if hasattr(self.CarringtonNE, 'as_dict') else self.CarringtonNE
        if self.CarringtonSW is not None:
            d['CarringtonSW'] = self.CarringtonSW.as_dict() if hasattr(self.CarringtonSW, 'as_dict') else self.CarringtonSW
        if self.StonyhurstSW is not None:
            d['StonyhurstSW'] = self.StonyhurstSW.as_dict() if hasattr(self.StonyhurstSW, 'as_dict') else self.StonyhurstSW
        return d

class FT__SolarSurface_BoundingBox:

    _event_type_enum = ['_SolarSurface_BoundingBox', ]
    _types_map = {
        'data': {'type': _SolarSurface_BoundingBox, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_SolarSurface_BoundingBox'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, _SolarSurface_BoundingBox):
            raise TypeError("data must be _SolarSurface_BoundingBox")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class SPOCA_CoronalHoleDetection:

    _types_map = {
        'Statistics': {'type': list, 'subtype': None},
        'AreaError': {'type': float, 'subtype': None},
        'Area': {'type': float, 'subtype': None},
        'Location': {'type': FT__HeliographicCoordinate, 'subtype': None},
        'BoundingBox': {'type': FT__SolarSurface_BoundingBox, 'subtype': None},
        'DetectionTime': {'type': str, 'subtype': None},
        'Contour': {'type': list, 'subtype': None},
    }
    _formats_map = {
        'DetectionTime': 'date-time',
    }

    def __init__(self
            , Statistics=None
            , AreaError=None
            , Area=None
            , Location=None
            , BoundingBox=None
            , DetectionTime=None
            , Contour=None
            ):
        self.Statistics = Statistics
        self.AreaError = AreaError
        self.Area = Area
        self.Location = Location
        self.BoundingBox = BoundingBox
        self.DetectionTime = DetectionTime
        self.Contour = Contour
    
    def _get_Statistics(self):
        return self.__Statistics
    def _set_Statistics(self, value):
        if value is None:
            self.__Statistics = value
            return
        if not isinstance(value, list):
            raise TypeError("Statistics must be list")
        self.__Statistics = value
    Statistics = property(_get_Statistics, _set_Statistics)
    
    def _get_AreaError(self):
        return self.__AreaError
    def _set_AreaError(self, value):
        if value is None:
            raise ValueError("AreaError cannot be None")
        if not isinstance(value, float):
            raise TypeError("AreaError must be float")
        self.__AreaError = value
    AreaError = property(_get_AreaError, _set_AreaError)
    
    def _get_Area(self):
        return self.__Area
    def _set_Area(self, value):
        if value is None:
            raise ValueError("Area cannot be None")
        if not isinstance(value, float):
            raise TypeError("Area must be float")
        self.__Area = value
    Area = property(_get_Area, _set_Area)
    
    def _get_Location(self):
        return self.__Location
    def _set_Location(self, value):
        if value is None:
            raise ValueError("Location cannot be None")
        if not isinstance(value, FT__HeliographicCoordinate):
            raise TypeError("Location must be FT__HeliographicCoordinate")
        self.__Location = value
    Location = property(_get_Location, _set_Location)
    
    def _get_BoundingBox(self):
        return self.__BoundingBox
    def _set_BoundingBox(self, value):
        if value is None:
            raise ValueError("BoundingBox cannot be None")
        if not isinstance(value, FT__SolarSurface_BoundingBox):
            raise TypeError("BoundingBox must be FT__SolarSurface_BoundingBox")
        self.__BoundingBox = value
    BoundingBox = property(_get_BoundingBox, _set_BoundingBox)
    
    def _get_DetectionTime(self):
        return self.__DetectionTime
    def _set_DetectionTime(self, value):
        if value is None:
            raise ValueError("DetectionTime cannot be None")
        if not isinstance(value, str):
            raise TypeError("DetectionTime must be str")
        self.__DetectionTime = value
    DetectionTime = property(_get_DetectionTime, _set_DetectionTime)
    
    def _get_Contour(self):
        return self.__Contour
    def _set_Contour(self, value):
        if value is None:
            self.__Contour = value
            return
        if not isinstance(value, list):
            raise TypeError("Contour must be list")
        self.__Contour = value
    Contour = property(_get_Contour, _set_Contour)
    
    def as_dict(self):
        d = dict()
        if self.Statistics is not None:
            d['Statistics'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Statistics]
        if self.AreaError is not None:
            d['AreaError'] = self.AreaError.as_dict() if hasattr(self.AreaError, 'as_dict') else self.AreaError
        if self.Area is not None:
            d['Area'] = self.Area.as_dict() if hasattr(self.Area, 'as_dict') else self.Area
        if self.Location is not None:
            d['Location'] = self.Location.as_dict() if hasattr(self.Location, 'as_dict') else self.Location
        if self.BoundingBox is not None:
            d['BoundingBox'] = self.BoundingBox.as_dict() if hasattr(self.BoundingBox, 'as_dict') else self.BoundingBox
        if self.DetectionTime is not None:
            d['DetectionTime'] = self.DetectionTime.as_dict() if hasattr(self.DetectionTime, 'as_dict') else self.DetectionTime
        if self.Contour is not None:
            d['Contour'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Contour]
        return d

class FT_SPOCA_CoronalHoleDetection:

    _event_type_enum = ['SPOCA_CoronalHoleDetection', ]
    _types_map = {
        'data': {'type': SPOCA_CoronalHoleDetection, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='SPOCA_CoronalHoleDetection'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, SPOCA_CoronalHoleDetection):
            raise TypeError("data must be SPOCA_CoronalHoleDetection")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class SPOCA_CoronalHole:

    _types_map = {
        'Polarity': {'type': float, 'subtype': None},
        'Detections': {'type': list, 'subtype': None},
        'EndTime': {'type': str, 'subtype': None},
        'BeginTime': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'EndTime': 'date-time',
        'BeginTime': 'date-time',
    }

    def __init__(self
            , Polarity=None
            , Detections=None
            , EndTime=None
            , BeginTime=None
            ):
        self.Polarity = Polarity
        self.Detections = Detections
        self.EndTime = EndTime
        self.BeginTime = BeginTime
    
    def _get_Polarity(self):
        return self.__Polarity
    def _set_Polarity(self, value):
        if value is None:
            self.__Polarity = value
            return
        if not isinstance(value, float):
            raise TypeError("Polarity must be float")
        self.__Polarity = value
    Polarity = property(_get_Polarity, _set_Polarity)
    
    def _get_Detections(self):
        return self.__Detections
    def _set_Detections(self, value):
        if value is None:
            self.__Detections = value
            return
        if not isinstance(value, list):
            raise TypeError("Detections must be list")
        self.__Detections = value
    Detections = property(_get_Detections, _set_Detections)
    
    def _get_EndTime(self):
        return self.__EndTime
    def _set_EndTime(self, value):
        if value is None:
            raise ValueError("EndTime cannot be None")
        if not isinstance(value, str):
            raise TypeError("EndTime must be str")
        self.__EndTime = value
    EndTime = property(_get_EndTime, _set_EndTime)
    
    def _get_BeginTime(self):
        return self.__BeginTime
    def _set_BeginTime(self, value):
        if value is None:
            raise ValueError("BeginTime cannot be None")
        if not isinstance(value, str):
            raise TypeError("BeginTime must be str")
        self.__BeginTime = value
    BeginTime = property(_get_BeginTime, _set_BeginTime)
    
    def as_dict(self):
        d = dict()
        if self.Polarity is not None:
            d['Polarity'] = self.Polarity.as_dict() if hasattr(self.Polarity, 'as_dict') else self.Polarity
        if self.Detections is not None:
            d['Detections'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Detections]
        if self.EndTime is not None:
            d['EndTime'] = self.EndTime.as_dict() if hasattr(self.EndTime, 'as_dict') else self.EndTime
        if self.BeginTime is not None:
            d['BeginTime'] = self.BeginTime.as_dict() if hasattr(self.BeginTime, 'as_dict') else self.BeginTime
        return d

class FT_SPOCA_CoronalHole:

    _event_type_enum = ['SPOCA_CoronalHole', ]
    _types_map = {
        'data': {'type': SPOCA_CoronalHole, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='SPOCA_CoronalHole'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if value is None:
            raise ValueError("data cannot be None")
        if not isinstance(value, SPOCA_CoronalHole):
            raise TypeError("data must be SPOCA_CoronalHole")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is None:
            self.__name = value
            return
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if value is None:
            raise ValueError("event_type cannot be None")
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.data is not None:
            d['data'] = self.data.as_dict() if hasattr(self.data, 'as_dict') else self.data
        if self.name is not None:
            d['name'] = self.name.as_dict() if hasattr(self.name, 'as_dict') else self.name
        if self.event_type is not None:
            d['event_type'] = self.event_type.as_dict() if hasattr(self.event_type, 'as_dict') else self.event_type
        return d

class RootObject:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
            ):
        pass
    
    def as_dict(self):
        d = dict()
        return d

